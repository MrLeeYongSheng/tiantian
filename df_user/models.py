#coding=utf-8
from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uphone = models.CharField(max_length=20,null=True,blank=True)
    uaddress = models.CharField(max_length=100,null=True,blank=True)
    uemail = models.CharField(max_length=40,null=True,blank=True)
    upostnum = models.CharField(max_length=6,null=True,blank=True)
