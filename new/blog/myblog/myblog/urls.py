
from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , get_home , name='Home'),
    url(r'^Home' , get_home , name='Home'),
    url(r'^Blog' , get_blog , name='Home'),
    url(r'^Contact' , get_contact, name='Home'),
    #url(r'^$' , get_blogs , name='blog_get_blogs'),
    #url(r'^detail/(\d+)/$', get_detail, name='blog_get_detail'),
]

