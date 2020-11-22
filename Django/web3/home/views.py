from django.shortcuts import render,reverse
from django.http import HttpResponse
from .models import Users
# Create your views here.
def index(r):
    return HttpResponse('hello')



def user_index(r):
    return HttpResponse('hello')

def user_add(r):
    if r.method == 'GET':
        return render(r,'user/add.html')
    else:
        data = r.POST.dict()
        data.pop('csrfmiddlewaretoken')
        try:
            obj = Users(**data)
            obj.save()
            url = reverse('user_index')
            return HttpResponse(f'<script>alert("提交成功");location.href="{url}"</script>')
        except:
            url = reverse('user_add')
            return HttpResponse(f'<script>alert("提交失败");location.href="{url}"</script>')

def user_delete(r):
    pass
def user_edit(r):
    pass