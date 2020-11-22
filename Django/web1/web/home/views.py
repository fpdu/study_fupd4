from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(r):
    # return HttpResponse('Hello World!')
    return render(r,'hello.html')