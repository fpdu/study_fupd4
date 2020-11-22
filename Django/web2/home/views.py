from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import json
from .models import Stu
# Create your views here.
def index(r):
    # return HttpResponse('HELLO WORLD')
    love = 'iloveyoutosimida'
    return render(r,'index.html',{'lovestr':love})
    # data = {'name':'张三丰','age':20,'sex':'m'}
    # return JsonResponse(data)
    # return HttpResponse(json.dumps(data))

    # return HttpResponseRedirect('/http/demo/')
def req_info(r):
    res = r.path
    print(res)
    return HttpResponse('关于请求对象')

def HttpDemo(r):
    method = r.method

    if method == 'GET':
        data = r.GET.dict()
    elif method == 'POST':
        data = r.POST.dict()
    print(data)

    return HttpResponse(f'当前请求方式:{method},接受的数据是{data}')

def tmpdemo(r):
    res = ['a','b','c']
    vardict = {'name':'张三丰','age':20}
    class Person():
        name = '张三'
        age = 20
        def func(self):
            return 'abcfunc....'
        def __str__(self):
            return '这是一个对象'
    obj = Person()

    # context = {'arr':res}
    varhtml = '<h1 style="color:red">love</h1>'
    context = {'arr':res,'var1dict':vardict,'obj1':obj,'var1html':varhtml}
    return render(r,'tmp.html',context)

def modemo(r):
    # obj = Stu()
    # obj.name = '张三丰'
    # obj.age = 20
    # obj.sex = '男'
    # obj.save()
    # data = {'name':'list','age':22,'sex':'女'}
    # obj = Stu(**data)
    # obj.save()

    # data = Stu.objects.filter(sex='女')
    # print(data)
    # for i in data:
    #     print(i)
    #     print(i.name)

    obj = Stu.objects.get(id=2)
    obj.name = '李思思'
    print(obj.name)
    obj.save()




    return HttpResponse('1111')