from django.shortcuts import render
from django.http import JsonResponse
from django.core.checks import messages
from django.shortcuts import render
from django.shortcuts import render
from django import template
from django.core import paginator
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from user.models import Friend, FriendRelationship, User,Wish
from news.models import PersonalArticle, User,Comment,Collect,SecondaryComment,Praise
from django.template.loader import get_template
from datetime import datetime, time
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.forms import model_to_dict
import json


def test(request):
    # data = {}
    article = PersonalArticle.objects.all().values()
    # data['result'] = json.loads(serializers.serialize('json',article))
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # data = []
    # for i in article:
    #     json_dict = model_to_dict(i)
    #     data.append(json_dict)
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    data = list(article)
    return JsonResponse(data, safe=False)


def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        try:
            if request.session.get('username', ''):
                 return JsonResponse({
                     'status': True,
                     'fail_message': '用户已登录'
                 })
            else:
                # 用户登录核实
                user = User.objects.get(username=username, password=password)
                # 是否核实正确
                if user:
                    request.session['username'] = username
                    return JsonResponse({
                        'username':request.session.get('username',''),
                        'status':True,
                        'success_message':'登录成功'
                    })
                else:
                    return JsonResponse({
                        'status': False,
                        'fail_message':'登录失败，用户名或密码密码错误'
                    })
        except:
            return JsonResponse({
                'status': False,
                'fail_message': '登录失败，用户名或密码密码错误'
            })


def logout(request):
    try:
        del request.session['username']
        return JsonResponse({
          'status': True,
          'messgae':'注销成功',
        })
    except:
        return JsonResponse({
            'status': False,
            'messgae': '注销失败',
        })


def my_publish(request):
    data = {}
    try:
        if 'username' in request.session:
            username = request.session['username']
        else:
            return JsonResponse({
                'status': False,
                'messgae': '请登录',
            })
        user = User.objects.get(username=username)
        articles = PersonalArticle.objects.filter(author=user).values()
        data['articles'] = list(articles)
        data['status'] = True
        # return JsonResponse(list(articles),safe=False)
        return JsonResponse(data)
    except:
        return JsonResponse({
            'status': False,
            'messgae': '请登录',
        })


def signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            introduction = request.POST.get('introduction')
            gender = request.POST.get('gender')
            # 查看用户名是否存在
            if User.objects.filter(username=username):
                return JsonResponse({
                    'status': False,
                    'messgae': '该用户名已存在',
                })
            else:
                # 创建新用户
                new_user = User.objects.create(username=username,
                                               password=password, email=email, gender=gender, introduction=introduction,
                                               status=True)
                new_user.save()
                return JsonResponse({
                    'status': True,
                    'messgae': '注册成功',
                })
    except:
        return JsonResponse({
            'status': False,
            'messgae': '注册失败',
        })
