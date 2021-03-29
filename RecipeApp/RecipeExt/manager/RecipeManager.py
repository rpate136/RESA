import json, datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Recipe, RecipeIngredient, Ingredient


# @csrf_exempt
# def chefRequest(request, chef_id=None):
# 	return HttpResponse(json.dumps({"success":True}), content_type="application/json")

@csrf_exempt
def recipeRequest(request, recipe_id=None):
	"""GET: 	Get a recipe by ID
	   POST: 	Add a new recipe to the database
	"""
	# Check if user is logged in 
	# Only logged in users can add/get a recipe

	if not request.user.is_authenticated: 
		response_data = {'success':False, 'error': "You need to be logged in to add or search for existing recipes"}
		return HttpResponse(json.dumps(response_data), content_type="application/json")

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
	title = request.POST.get('title', '')
	_rawIngredientsList = request.POST.get('ingredients', [])
	directions = request.POST.get('directions', '')
	_prep_time = request.POST.get('prep_time', {'minutes':0, 'hours':0})
	_cook_time = request.POST.get('cook_time', '')
	_total_time = request.POST.get('total_time', '')
	serving_size = request.POST.get('serving_size', '')
	nutritional_info = request.POST.get('nutritional_info', '')
	thumbnail_url = request.POST.get('thumbnail_url', '')
	source = request.POST.get('source', '')
	user = request.user

	# Currently we're not checking if the recipe is unique in any way
	recipe = Recipe()
	recipe.title = title
	recipe.directions = directions
	recipe.serving_size = serving_size
	recipe.nutritional_info = nutritional_info
	recipe.thumbnail_url = thumbnail_url
	recipe.source = source
	
	# Clean Prep Time: 
	_prep_time = json.loads(_prep_time)
	prep_time = datetime.timedelta(minutes=_prep_time['minutes'], hours=_prep_time['hours'])
	recipe.prep_time = prep_time

	_cook_time = json.loads(_cook_time)
	cook_time = datetime.timedelta(minutes=_cook_time['minutes'], hours=_cook_time['hours'])
	recipe.cook_time = cook_time

	_total_time = json.loads(_total_time)
	total_time = datetime.timedelta(minutes=_total_time['minutes'], hours=_total_time['hours'])
	recipe.total_time = total_time

	recipe.chef = user.chef
	recipe.save()


	# Associate later
	# print("Added Ingredients: ", _rawIngredientsList)

	# Eg. {"name":"Apple", "ingredient_string":"one cup of chopped apples", "quantity":"1", "unit":"cup"}

	_rawIngredientsList = json.loads(_rawIngredientsList)
	for _ingredient in _rawIngredientsList: 
		ingredients = Ingredient.objects.filter(name=_ingredient['name'])
		if len(ingredients) > 0: 
			# Ingredient exists
			ingredient = ingredients[0]

		else: 
			# Ingredient doesn't exist.
			# Make new ingredient and add to the db
			ingredient = Ingredient(name=_ingredient['name'])
			ingredient.save()

		recipe_ingredient = RecipeIngredient.objects.create(
			recipe = recipe,
			ingredient = ingredient,
			ingredient_string = _ingredient['ingredient_string'],
			quantity = _ingredient['quantity'],
			unit = _ingredient['unit'],
			available = True
		)

	response_data = recipe.getResponseData()
	print("Reached Here: ", response_data)

	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def getRecipe(request, recipe_id):
	response_data = {}
	
	if recipe_id:
		recipes = Recipe.objects.filter(id=recipe_id)

		if len(recipes)>0:
			recipe = recipes[0]
			response_data = recipe.getResponseData()

		else:
			errorMessage = "Error! This recipe doesn't exist."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")

