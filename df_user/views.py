#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from hashlib import sha1
# Create your views here.

def register(request):
    return render(request,'register.html')

def register_handler(request):
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    allow = post.get('allow')
    #print("%s %s %s %s %s"%(user_name,pwd,cpwd,email,allow))
    #判断是否勾选协议
    #判断用户名或者密码是否为空
    if 'on'==allow and user_name and pwd:
        #判断密码是否2次都相同
        if pwd==cpwd:
            s = sha1()
            s.update(pwd.encode('utf-8'))
            sha1_pwd = s.hexdigest()
            user = UserInfo()
            user.uname = user_name
            user.upwd = sha1_pwd
            user.uemail = email
            user.save()
            #验证通过,存进数据库,并且重定向到index首页
            return render(request,'index.html')
    return render(request, 'register.html', {'message':'<h1>年轻人,别搞事!</h1>'})

def login(request):
    return render(request,'login.html')

def login_handler(request):
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    if username and pwd:
        s = sha1()
        s.update(pwd.encode('utf-8'))
        sha1_pwd = s.hexdigest()
        try:
            qpwd = UserInfo.objects.filter(uname=username)[0]
        except:
            #没有该用户,用户名错误
            return render(request, 'login.html', {'message': ',用户名错误,年轻人,别搞事!'})
        else:
            if not qpwd:
                # 没有该用户,用户名错误
                return render(request, 'login.html', {'message': ',用户名错误,年轻人,别搞事!'})
            #用户存在
            if qpwd.upwd == sha1_pwd:
                #密码正确
                return render(request, 'index.html')
            else:
                #密码错误
                return render(request, 'login.html', {'message': ',密码错误,年轻人,别搞事!'})