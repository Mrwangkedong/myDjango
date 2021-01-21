from django.db import models
# Create your models here.


# json化
class BaseModel(models.Model):
    class Meta:
        abstract = True

    # 返回self._meta.fields中没有的，但是又是需要的字段名的列表
    # 形如['name','type']
    def getMtMField(self):
        pass

    # 返回需要在json中忽略的字段名的列表
    # 形如['password']
    def getIgnoreList(self):
        pass

    def isAttrInstance(self, attr, clazz):
        return isinstance(getattr(self, attr), clazz)

    def getDict(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        import datetime
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr), datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            # 特殊处理datetime的数据
            elif isinstance(getattr(self, attr), BaseModel):
                d[attr] = getattr(self, attr).getDict()
            # 递归生成BaseModel类的dict
            elif self.isAttrInstance(attr, int) or self.isAttrInstance(attr, float) \
                    or self.isAttrInstance(attr, str):
                d[attr] = getattr(self, attr)
            # else:
            #     d[attr] = getattr(self, attr)

        mAttr = self.getMtMField()
        if mAttr is not None:
            for m in mAttr:
                if hasattr(self, m):
                    attlist = getattr(self, m).all()
                    l = []
                    for attr in attlist:
                        if isinstance(attr, BaseModel):
                            l.append(attr.getDict())
                        else:
                            dic = attr.__dict__
                            if '_state' in dic:
                                dic.pop('_state')
                            l.append(dic)
                    d[m] = l
        # 由于ManyToMany类不能存在于_meat.fields，因而子类需要在getMtMFiled中返回这些字段
        if 'basemodel_ptr' in d:
            d.pop('basemodel_ptr')

        ignoreList = self.getIgnoreList()
        if ignoreList is not None:
            for m in ignoreList:
                if d.get(m) is not None:
                    d.pop(m)
        # 移除不需要的字段
        return d

    def toJSON(self):
        import json
        return json.dumps(self.getDict(), ensure_ascii=False).encode('utf-8').decode()


#公安局
class Group(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    def get_companies(self):
        return self.group_company.all()

# 大队
class Company(BaseModel):
    name = models.CharField(max_length=32)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,default='', related_name='group_company',blank=True)
    def get_department(self):
        return self.company_depart.all()
    def get_parsons(self):
        return self.per_company.all()
# 小队
class Department(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,default='', related_name='company_depart',blank=True)
    def get_persons(self):
        return self.per_dep.all()


#成员
class Person(BaseModel):
    p_id = models.AutoField(primary_key=True,blank=True)
    name = models.CharField(max_length=32)#姓名
    phone_number = models.CharField(max_length=11,default='')#手机号
    email = models.CharField(max_length=32,default='')#邮箱
    password = models.CharField(max_length=32,default='123456')#密码，默认为123456
    level = models.IntegerField()#等级
    group = models.ForeignKey(Group,related_name='per_group',on_delete=models.CASCADE,default='',blank=False)#所属集团，不为空
    company = models.ForeignKey(Company, related_name='per_company', on_delete=models.CASCADE,default='')#所属公司
    department = models.ForeignKey(Department, related_name='per_dep', on_delete=models.CASCADE,default='')#所属部门

    def __str__(self):
        return str(self.p_id)


#权限，无用
class Power(BaseModel):
    p_id = models.ForeignKey(Person,on_delete=models.CASCADE,default='', related_name='person_power')
    kill = models.BooleanField(default=False)#遥毙
    radio_call = models.BooleanField(default=True)  #广播呼叫
    real_time_video = models.BooleanField(default=True)     #实时视频
    incoming_call = models.BooleanField(default=True)  #临时呼叫呼入
    out_call = models.BooleanField(default=True)    #临时呼叫呼出
    FM_call = models.BooleanField(default=True)     #频道呼叫
    enterprise_control = models.BooleanField(default=False)     #企业调度权限，默认False



#聊天室，无用
class Chat(BaseModel):
    name = models.CharField(max_length=32)
    creater = models.ForeignKey(Person,on_delete=models.CASCADE,default='',related_name='per_talkcreter')
    users = models.ManyToManyField(Person)

    def getMtMField(self):
        return ['users']


#频道，无用
class Fm(BaseModel):
    name = models.CharField(max_length=32)
    creater = models.ForeignKey(Person,on_delete=models.CASCADE,default='',related_name='per_fmcreater')
    users = models.ManyToManyField(Person)
    info = models.CharField(max_length=200)
    max_persons = models.IntegerField(default=20)#最大人数，默认为20人

# 无用
def getMtMField(self):
    return ['users']


