from django.urls import path
from . import views
from .manager import UserManager

urlpatterns = [
	# User Interface redirect/views
    path('', views.index, name='index'),


    # API Interface
	path('api/chef/', UserManager.chefRequest),     
	# path(r'api/chef/(?P<chef_id>\d*)/$', UserManager.chefRequest)

	path('api/chef/<int:chef_id>/', UserManager.chefRequest, name="chefRequest")
]