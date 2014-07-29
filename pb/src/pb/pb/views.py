# -*- coding:utf-8 -*-
'''

@author: Administrator
'''
from django.shortcuts import  render_to_response

#首页
def index(request):
    print 'index'
    return render_to_response('index.html')
#关于页面
def about(request):
    print 'about'
    return render_to_response('about.html')

