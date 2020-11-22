from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('user/index/',views.user_index,name='user_index'),
    path('user/add/',views.user_add,name='user_add'),
    path('user/delete/',views.user_delete,name='user_delete'),
    path('user/edit/',views.user_edit,name='user_edit'),

]
