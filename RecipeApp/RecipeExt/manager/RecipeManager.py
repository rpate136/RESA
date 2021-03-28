import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Recipe, RecipeIngredient, Ingredient


# @csrf_exempt
# def chefRequest(request, chef_id=None):
# 	return HttpResponse(json.dumps({"success":True}), content_type="application/json")

@csrf_exempt
def recipeRequest(request, recipe_id=None):
	if request.method == "POST":
		return createRecipe(request)

	else:
		return getRecipe(request, recipe_id)
	return HttpResponse(json.dumps(response_data), content_type="application/json")


# Creating new chef
@csrf_exempt
def createRecipe(request):
	response_data = {}

	# Check for logged in User
	# title = request.POST.get('title', '')
	# ingredients = request.POST.get('ingredients', '')
	# directions = request.POST.get('directions', '')
	# prep_time = request.POST.get('prep_time', '')
	# cook_time = request.POST.get('cook_time', '')
	# total_time = request.POST.get('total_time', '')
	# serving_size = request.POST.get('serving_size', '')
	# nutritional_info = request.POST.get('nutritional_info', '')
	# thumbnail_url = request.POST.get('thumbnail_url', '')
	# source = request.POST.get('source', '')
	# author = request.POST.get('author', '')



	# recipe = None
	# existing_recipe = Chef.objects.filter(source=source)

	# if len(existing_chefs) > 0:
	# 	# chef Exists!
	# 	chef = existing_chefs[0]
	# 	errorMessage = "Error! Chef with this email already exists."

	# 	return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	# if chef is None:
	# 	chef = Chef()
	
	# chef.first_name = first_name
	# chef.last_name = last_name
	# chef.email = email
	# chef.save()

	# response_data = chef.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def getRecipe(request, recipe_id):
	response_data = {}
	
	if recipe_id:
		chefs = Recipe.objects.filter(id=recipe_id)

		if len(chefs)>0:
			chef = chefs[0]
			response_data = chef.getResponseData()

		else:
			errorMessage = "Error! This chef doesn't exist."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")

