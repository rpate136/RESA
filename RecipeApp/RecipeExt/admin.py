from django.contrib import admin

# Register your models here.

from .models import Chef, Recipe, RecipeIngredient, Ingredient

admin.site.register(Chef)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)