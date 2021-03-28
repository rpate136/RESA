from django.urls import path
from . import views
from .manager import UserManager, IngredientManager, RecipeManager

urlpatterns = [
	# User Interface redirect/views
    path('', views.index, name='index'),


    # API Interface
    # URL Format: 127.0.0.1:8000/api/____ 
    # Eg. 127.0.0.1:8000/api/chef/1/ ----> GET Chef with ID 1 
    

    #Chef - User Creation / Get User 
	path('chef/', UserManager.chefRequest),     
	path('chef/<int:chef_id>/', UserManager.chefRequest, name="chefRequest"),
	path('chef/login/', UserManager.chefLogin),
	path('chef/logout/', UserManager.chefLogout),

    #Ingredients
	path('ingredient/', IngredientManager.ingredientRequest),     
	path('ingredient/<int:ingredient_id>/', IngredientManager.ingredientRequest, name="ingredientRequest"),

	# Quantity
	path('recipe/', RecipeManager.recipeRequest),     
	path('recipe/<int:recipe_id>/', RecipeManager.recipeRequest, name="recipeRequest")

]


