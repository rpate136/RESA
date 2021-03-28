from django.urls import path
from . import views
from .manager import UserManager, IngredientManager

urlpatterns = [
	# User Interface redirect/views
    path('', views.index, name='index'),


    # API Interface
        #Chefs
	path('api/chef/', UserManager.chefRequest),     
	path('api/chef/<int:chef_id>/', UserManager.chefRequest, name="chefRequest"),

        #Ingredients
	path('api/ingredient/', IngredientManager.ingredientRequest),     
	path('api/ingredient/<int:ingredient_id>/', IngredientManager.ingredientRequest, name="ingredientRequest")
]


