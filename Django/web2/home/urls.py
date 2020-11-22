from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.index),
    path('req/info/',views.req_info),
    path('http/demo/',views.HttpDemo,name='HttpDemo'),
    path('tmp/demo/',views.tmpdemo,name='tmpdemo'),
    path('mod/demo/',views.modemo),


]