from django.db import models

# Create your models here.
class Stu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    sex = models.CharField(max_length=1,default='男')

class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    email = models.EmailField()
    scoure = models.DecimalField(max_digits=5,decimal_places=2)
    SEX_CHOICES = [(1,'男'),(0,'女')]
    sex = models.IntegerField(choices=SEX_CHOICES)