from django.urls import path

from . import views

from .manager import UserManager

urlpatterns = [
	# User Interface redirect/views
    path('', views.index, name='index'),


    # API Interface
    path(r'^api/chef/$', UserManager.chefRequest),     
	path(r'^api/chef/(?P<chef_id>\d*)/$', UserManager.chefRequest)
]