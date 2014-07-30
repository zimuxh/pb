# -*- coding:utf-8 -*-
'''

@author: Administrator
'''
from django.shortcuts import  render_to_response,render
from model import Article, Posts
#from django.contrib.auth.models import User
#首页
def index(request):
    print 'index'
    return render_to_response('index.html')
#关于页面
def about(request):
    print 'about'
    return render_to_response('about.html')
#文章列表页面
def list(request):
    print 'list'
    #article =  Article()
    all = Posts.objects.all();
    for i in all:
        print i.id
    return render(request,'page.html',{'all':all})
