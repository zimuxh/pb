'''
Created on 

@author: Administrator
'''
#coding=utf-8
from django.shortcuts import  render_to_response
'''
from django.http import HttpResponse
def index(request):
    print 'ht'
    return HttpResponse('pb/html/index.html');
'''
def index(request):
    print 'index'
    return render_to_response('index.html');