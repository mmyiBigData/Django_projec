from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^forms', views.forms,name='forms'),
	url(r'^add_record', views.add_record, name='add_record'),
	# url(r'^list', views.list,name='list'),
	url(r'^(?P<id>^\d+)', views.list,name='list'),
	url(r'^index', views.index,name='index'),
	url(r'^$', views.index,name='index'),
]
