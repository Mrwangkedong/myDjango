from django.shortcuts import render,HttpResponse
# python manage.py runserver 0.0.0.0:8000
from django.http import HttpResponse,JsonResponse
import json

from . import models
from company_app.models import Person,Group,Department,Company,BaseModel
# Create your views here.


def delete_person(request):
    import re
    # # 业务逻辑代码
    big_id = (request.POST.get('big_id'))
    new = []
    big_id=big_id[1:-1]
    data = (re.findall("\"(.*?)\"", big_id))
    for i in range(len(data)):
        data[i] = int(data[i])

    for item in data:
        try:
            person = Person.objects.get(pk=item).delete()
        except:
            return HttpResponse(0)
    return HttpResponse(1)

#获取所有大队信息
def all_big(request):
    police = Group.objects.get(pk=101)
    all_big = police.get_companies().values()
    all_big_list = list(all_big)
    return JsonResponse(all_big_list, safe=False)

# 获取单个大队信息
def getbig(request):
    big_id = (request.POST.get('big_id'))
    big_id = big_id
    print(big_id)
    big = models.Company.objects.get(pk=big_id).toJSON()

    return  HttpResponse(big)

#获得大队队长信息
def get_big_captain(request):
    big_id = (request.POST.get('big_id'))
    try:
        big_duizhangs = Person.objects.filter(level=3, company_id=big_id).values()
        big_duizhangs = list(big_duizhangs)
        return JsonResponse(big_duizhangs,safe=False)
    except:
        data = {
            'name' : '暂无',
            'p_id' : 00,
        }
        return HttpResponse(json.dumps(data))

#获得大队（big_id）下的所有小队
def get_small(request):
    big_id = (request.POST.get('big_id'))
    print('得到大对虾的所有小队',big_id)
    smalls = models.Company.objects.get(pk=big_id).get_department().values()
    smalls_list = list(smalls)

    return JsonResponse(smalls_list,safe=False)

#根据小队信息获取小队人员
def get_small_person(request):
    small_id = (request.POST.get('send_small_id'))
    print(small_id)
    small = Department.objects.get(pk=small_id)
    small_persons = small.get_persons().values()
    small_persons_list = list(small_persons)
    print(small_persons)
    return JsonResponse(small_persons_list, safe=False)

#添加新的小队信息
def add_small(request):
    small_name = request.POST.get('small_name')
    big_id = request.POST.get('big_id')
    print(small_name)
    print(big_id)
    try:
        Department.objects.create(name=small_name, company_id=big_id)
    except:
        return HttpResponse(0)

    return HttpResponse(1)

#添加新的小队信息
def add_big(request):
    big_name = request.POST.get('big_name')
    print(big_name)
    try:
        Company.objects.create(name=big_name,group_id=101)
    except:
        return HttpResponse(0)

    return HttpResponse(1)

#获取成员个人信息
def get_person_info(request):
    person_id = request.POST.get('send_person_id')
    print(person_id)
    person_info = Person.objects.get(pk=person_id).toJSON()
    return HttpResponse(person_info)

#从前端获取更改后的信息，并进行修改
def edit_person_info(request):
    username = request.POST.get('username')

    name = request.POST.get('name')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')
    police = request.POST.get('police')
    level = request.POST.get('level')
    big = request.POST.get('big')
    small = request.POST.get('small')
    print(small)

    person = Person.objects.get(pk=username)
    person.name = name
    person.password = password
    person.phone_number = phone_number
    person.email=email
    person.level = level
    person.company_id=big
    person.department_id=small
    person.save()

    return HttpResponse(big)


#增加新队员
def new_person_info(request):
    name = request.POST.get('name')
    print(name)
    password = request.POST.get('password')
    print(password)
    phone_number = request.POST.get('phone_number')
    print(phone_number)
    email = request.POST.get('email')
    print(email)
    level = request.POST.get('level')
    print(level)
    big = request.POST.get('big')
    print(big)
    small = request.POST.get('small')
    print(small)


    Person.objects.create(name=name,password=password,phone_number=phone_number,email=email,level=level,company_id=big,department_id=small,group_id=101)
    person = Person.objects.get(name=name,password=password)


    return HttpResponse(person.p_id)
