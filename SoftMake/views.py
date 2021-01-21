from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . import models
from SoftMake.models import HtSign
import json
# Create your views here.
# python manage.py runserver 0.0.0.0:8000

def GoIndex(request):

    return render(request,'SoftMake/index.html')

def GetAll(request):

    #获得从前端表单传回的值
    HT = []
    ht_num = request.POST.get('ht_num','')
    HT.append(ht_num)
    ybs_num = request.POST.get('ybs_num','')
    HT.append(ybs_num)
    tb_num = request.POST.get('tb_num','')
    HT.append(tb_num)
    jia_name = request.POST.get('jia_name','')
    HT.append(jia_name)
    yi_name = request.POST.get('yi_name','')
    HT.append(yi_name)
    start_data = request.POST.get('start_data','')
    HT.append(start_data)
    end_data = request.POST.get('end_data','')
    HT.append(end_data)
    ht_money =request.POST.get('ht_money','')
    HT.append(ht_money)
    jia_leader = request.POST.get('jia_leader','jia_leader')
    HT.append(jia_leader)
    yi_leader = request.POST.get('yi_leader','yi_leader')
    HT.append(yi_leader)
    ht_content = request.POST.get('ht_content','')
    HT.append(ht_content)
    ht_remark = request.POST.get('ht_remark','')
    HT.append(ht_remark)

    #检测是否有空值存在
    for i in range(len(HT)):
        if HT[i] == '':
            print(i,HT[i])
            return HttpResponse('不能有空!返回重新填写！')
    #查看是否已经存在
    try:
        HtSign.objects.get(ht_num=ht_num) #查找数据项
        return HttpResponse('已存在!')
    except:
        #写入数据库
        HtSign.objects.create(ht_num=ht_num, ybs_num=ybs_num, tb_num=tb_num, jia_name=jia_name, yi_name=yi_name,
                              start_data=start_data, end_time=end_data, ht_money=ht_money, jia_leader=jia_leader,
                              yi_leader=yi_leader, ht_content=ht_content, ht_remark=ht_remark)

        return HttpResponse('ok!')
