from django.db import models

# Create your models here.
#合同书的主要内容
class HtSign(models.Model):
    HtSign_num = models.AutoField(primary_key=True)  #主键，自动生成
    ht_num = models.CharField(max_length=11) #合同编号
    ybs_num = models.CharField(max_length=11) #邀标书编号
    tb_num = models.CharField(max_length=11)    #投标编号
    jia_name = models.CharField(max_length=32) #甲方姓名
    yi_name = models.CharField(max_length=32) #乙方姓名
    start_data = models.DateTimeField() #开始时间
    end_time = models.DateTimeField() #结束时间
    ht_money = models.CharField(max_length=11) #合同金额
    jia_leader = models.CharField(max_length=32) #甲方代表
    yi_leader = models.CharField(max_length=32) #乙方代表
    ht_content = models.TextField() #合同内容
    ht_remark = models.TextField() #合同备注