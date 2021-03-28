import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from ..models import Ingredient


@csrf_exempt
def ingredientRequest(request, ingredient_id=None):
	if request.method == "POST":
		return createIngredient(request)
	else:
		return getIngredient(request, ingredient_id)
	return HttpResponse(json.dumps({'success': False, "error":"Unable to complete request"}), content_type="application/json")


#Create New Ingredient
@csrf_exempt
def createIngredient(request):
	name = request.POST.get('name', '')

	ingredient = None
	existing_ingredients = Ingredient.objects.filter(name=name)

	if len(existing_ingredients) > 0:
		# ingredient Exists!
		ingredient = existing_ingredients[0]
		errorMessage = "Error! This ingredient already exists."

		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if ingredient is None:
		ingredient = Ingredient()
	
	ingredient.name = name
	ingredient.save()
	response_data = ingredient.getResponseData()

	return HttpResponse(json.dumps(response_data), content_type="application/json")


#Get Ingredient by ID
@csrf_exempt
def getIngredient(request, ingredient_id):
	response_data = {}
	
	if ingredient_id:
		ingredients = Ingredient.objects.filter(id=ingredient_id)
		

		if len(ingredients)>0:
			ingredient = ingredients[0]
			response_data = ingredient.getResponseData()

		else:
			errorMessage = "Error! This ingredient doesn't exist."
			response_data = {'success': False, "error":errorMessage}

	return HttpResponse(json.dumps(response_data), content_type="application/json")




