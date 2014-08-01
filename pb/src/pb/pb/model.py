# -*- coding:utf-8 -*-
'''
Created on 2014年7月29日

@author: Administrator
'''
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 10)
    time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length = 1000)
    group = models.IntegerField(max_length = 7)
    def __unicode__(self):
        return self.title
    
class Posts(models.Model):
    post_author = models.IntegerField()
    post_date = models.DateField()
    post_date_gmt = models.DateField()
    post_content = models.CharField()
    post_title = models.CharField()
    post_excerpt = models.CharField()
    post_status = models.CharField()
    comment_status = models.CharField()
    ping_status = models.CharField()
    post_password = models.CharField()
    def __unicode__(self):
        return self.post_content
    
