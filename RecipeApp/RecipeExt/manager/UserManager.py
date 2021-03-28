import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Chef
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


@csrf_exempt
def chefLogin(request):
	email = request.POST['email']
	password = request.POST['password']
	user = authenticate(request, username=email, password=password)

	# # The Django auth backend authenticates the user
	if user is not None:
		login(request, user)
		response_data = {'success':True, "message": "You have been successfully logge in, %s!"%(user.first_name)}
	else:
		# Return an 'invalid login' error message.
		response_data = {'success':False, "message": "Either your email or password is incorrect, or doesn't exist in our system."}
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def chefLogout(request):
	# The Django backend logs out the user
    logout(request)


@csrf_exempt
def chefRequest(request, chef_id=None):
	print(request.user, request.user.is_authenticated)
	if request.method == "POST":
		return createChef(request)

	else:
		return getChef(request, chef_id)

	return HttpResponse(json.dumps(response_data), content_type="application/json")


# Creating new chef
@csrf_exempt
def createChef(request):

	first_name = request.POST.get('first_name', '')
	last_name = request.POST.get('last_name', '')
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	about_me = request.POST.get('about_me', '')
	location = request.POST.get('location', '')

	# username is the same as email 
	user = User.objects.create_user(email, email, password)
	user.first_name = first_name
	user.last_name = last_name

	user.save()

	chef = Chef.objects.create(user=user)
	chef.about_me = about_me
	chef.location = location
	chef.save()

	response_data = chef.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def getChef(request, chef_id):
	response_data = {}
	
	if chef_id:
		chefs = Chef.objects.filter(id=chef_id)

		if len(chefs)>0:
			chef = chefs[0]
			response_data = chef.getResponseData()

		else:
			errorMessage = "Error! This chef doesn't exist."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")

