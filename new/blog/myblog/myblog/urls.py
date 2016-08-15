
from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , get_blogs , name='blog_get_blogs'),
    url(r'^detail/(\d+)/$', get_detail, name='blog_get_detail'),
]

