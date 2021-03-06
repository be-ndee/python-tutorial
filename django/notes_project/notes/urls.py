from django.conf.urls import patterns, url

from notes import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<note_id>\d+)/$', views.show, name='show'),
	url(r'^(?P<note_id>\d+)/edit/$', views.edit, name='edit'),
	url(r'^(?P<note_id>\d+)/delete/$', views.delete, name='delete'),
	url(r'^new/$', views.new, name='new')
)
