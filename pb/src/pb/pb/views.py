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
   
    return render_to_response('index.html')
#关于页面
def about(request):
    
    return render_to_response('about.html')
#文章列表页面        param:文章的分类  当为0时  表示全部    
def list(request):
    param = request.GET.get("param")
    if param == None:
        all = Article.objects.all()
    else:
        all =  Article.objects.filter(group = param)
    return render(request,'main.html',{'all':all})
#文章保存页面
def editor(request):
    content = request.POST['content']
    title = request.POST['title']
    article = Article(title=title,content=content,group='1');
    article.save()
    result = "文章保存成功！"
    print result
    return HttpResponse(result, mimetype='application/javascript')

#
def pagelist(request):
    all = Article.objects.all()
    return render(request,'admin/pagelist.html',{'all':all})