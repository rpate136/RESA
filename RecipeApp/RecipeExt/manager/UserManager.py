import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Chef


# @csrf_exempt
# def chefRequest(request, chef_id=None):
# 	return HttpResponse(json.dumps({"success":True}), content_type="application/json")

@csrf_exempt
def chefRequest(request, chef_id=None):
	if request.method == "POST":
		# errorMessage = "TODO POST"
		# response_data = {'success': True, "error":errorMessage}
		return createChef(request)
		# return response_data 
	else:
		# errorMessage = "TODO GET"
		# response_data = {'success': True, "error":errorMessage}
		return getChef(request, chef_id)
	return HttpResponse(json.dumps(response_data), content_type="application/json")


# Creating new chef
@csrf_exempt
def createChef(request):
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	email = request.POST.get('email','')

	chef = None
	existing_chefs = Chef.objects.filter(email=email)

	if len(existing_chefs) > 0:
		# chef Exists!
		chef = existing_chefs[0]
		errorMessage = "Error! Chef with this email already exists."

		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if chef is None:
		chef = Chef()

	chef.first_name = first_name
	chef.last_name = last_name
	chef.email = email
	
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

