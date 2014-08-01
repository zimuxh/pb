# -*- coding:utf-8 -*-
'''

@author: Administrator
'''
from django.shortcuts import  render_to_response,render
from django.http import HttpResponse
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
#文章列表页面        param:文章的分类  当为0时  表示全部
def list(request):
    param = request.GET.get("param")
    if param == None:
        all = Article.objects.all()
    else:
        all =  Article.objects.filter(group = param)
    print all   
    #all = Posts.objects.filter(post_author=2);
    return render(request,{'all':all})
#
def article(request):
    all = Posts.objects.all(post_author=2)
    return HttpResponse(all)
