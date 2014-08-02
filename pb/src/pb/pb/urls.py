
from django.conf.urls import patterns, url

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    (r'^js/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.JS_STATIC_PATH}),
    
    #(r'^css/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.CSS_STATIC_PATH}),
    
    #(r'^html/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.HTML_STATIC_PATH}),
    
    #(r'^images/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.IMAGES_STATIC_PATH}),
    
    url(r'^$', 'pb.views.index'),

    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC}),
    
    url(r'^admin/', 'pb.views.toLogin'),
                       
    url(r'^index$', 'pb.views.index'),
    
    url(r'^about$', 'pb.views.about'),
    
    url(r'^list$', 'pb.views.list'),
    
    url(r'^editor$', 'pb.views.editor'),
)