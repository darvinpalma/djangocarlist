from django.conf.urls import url
from . import views

app_name = 'carlistapp'

urlpatterns = [
	url(r'^$', views.homeview, name='home'),
	url(r'^home/$', views.homeview, name='home'),
	url(r'^editposition/$', views.editposition, name='editposition'),
	url(r'^choosecolor/$', views.choosecolor, name='choosecolor'),
]