from django.conf.urls import *

from HelloWord.view import hello

urlpatterns = patterns("",
	('^hello/$', hello),
)