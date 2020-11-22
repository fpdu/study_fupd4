from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=5)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    age = models.IntegerField()
    SEX_CHOICE = [(1,'男'),(0,'女')]
    sex = models.IntegerField(choices=SEX_CHOICE)
    creatime = models.DateTimeField(auto_now_add=True)
    updatetime = models.DateTimeField(auto_now=True)