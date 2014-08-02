# -*- coding:utf-8 -*-
'''

@author: Administrator
'''
from django.shortcuts import  render_to_response,render

from django.http import HttpResponse

from model import Article

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
    return render(request,'main.html',{'all':all})

def editor(request):
    content = request.POST['content']
    title = request.POST['title']
    article = Article(title=title,content=content,group='1');
    print article
    article.save()
    result = 1
    print result
    return HttpResponse(result, mimetype='application/javascript')

def toLogin(request):
    return render(request,'admin/login.html')