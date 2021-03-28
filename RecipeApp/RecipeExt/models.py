from django.db import models
import json, re, datetime
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


# Create your models here.

class Chef(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	about_me = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)

	def getResponseData(self):
		responseData = {}
		responseData["chef_id"]=self.id
		responseData["first_name"]=self.user.first_name
		responseData["last_name"]=self.user.last_name
		responseData["email"]=self.user.email
		responseData["about_me"]=self.about_me
		responseData["location"]=self.location

		return responseData

	def __unicode__(self):
		return "%s %s"%(self.user.first_name,self.user.last_name)

	def __str__(self):
		return "%s %s"%(self.user.first_name,self.user.last_name)

	def __hash__(self):
		return self.id

	def __cmp__(self, other):
		return self.id - other.id

	# def get_absolute_url(self):
	# 	"""Returns the url to access a detail record for this user."""
	# 	return reverse('chef-detail', args=[str(self.id)])

	class Meta:
		ordering = ('user',)


class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	# eg. name from Spoonacular -- cocoa powder

	def getResponseData(self):
		responseData = {}
		responseData["ingredient_id"]=self.id
		responseData["name"]=self.name

		return responseData

	def __unicode__(self):
		return "%s"%(self.name)

	def __str__(self):
		return "%s"%(self.name)

	def __hash__(self):
		return self.id

	def __cmp__(self, other):
		return self.id - other.id

	class Meta:
		ordering = ('name',)



class Recipe(models.Model):
	title = models.CharField(max_length=50)
	ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
	directions = models.CharField(max_length=5000)
	prep_time = models.DurationField(blank=True, null=True)
	cook_time = models.DurationField(blank=True, null=True)
	total_time = models.DurationField(blank=True, null=True)
	serving_size = models.IntegerField(default=1)
	nutritional_info = models.CharField(max_length=200, blank=True)
	thumbnail_url = models.URLField(max_length=100, blank=True) 
	source = models.URLField(max_length=100, blank=True) 

	# Check whether we need to not delete
	chef = models.ForeignKey(Chef, on_delete=models.CASCADE)

	def getResponseData(self):
		responseData = {}
		responseData["recipe_id"] = self.id
		responseData["title"] = self.title
		responseData["directions"] = self.directions
		responseData["serving_size"] = self.serving_size
		responseData["nutritional_info"] = self.nutritional_info
		responseData["thumbnail_url"] = self.thumbnail_url
		responseData["source"] = self.source
		responseData["chef_id"] = "%s"%(self.chef.id)

		responseData["prep_time"] = str(self.prep_time)
		responseData["cook_time"] = str(self.cook_time)
		responseData["total_time"] = str(self.total_time)

		ingredients = []
		_ingredientsList = RecipeIngredient.objects.filter(recipe=self)
		for eachIngredient in _ingredientsList: 
			ingredient = {}
			ingredient['name'] = eachIngredient.ingredient.name
			ingredient['ingredient_string'] = eachIngredient.ingredient_string
			ingredient['quantity'] = eachIngredient.quantity
			ingredient['unit'] = eachIngredient.unit
			ingredient['available'] = eachIngredient.available
			ingredients.append(ingredient)

		responseData["ingredients"] = ingredients

		return responseData

	def __unicode__(self):
		return "%s"%(self.title)

	def __str__(self):
		return "%s"%(self.title)

	def __hash__(self):
            	return self.id

	def __cmp__(self, other):
		return self.id - other.id

	# def get_absolute_url(self):
	# 	"""Returns the url to access a detail record for this book."""
	# 	return reverse('recipe-detail', args=[str(self.id)])

	class Meta:
		ordering = ('title',)


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	
	# Original ingredient string: eg. 1 cup of good quality cocoa powder, sifted
	ingredient_string = models.CharField(max_length=50)
	quantity = models.CharField(max_length=50)
	unit = models.CharField(max_length=10)

	# If available=false --> show in grocery list
	available = models.BooleanField(default=True)

	def set_ingredient(self, ingredient_string):
		ingredient = [Ingredient.objects.filter(name=word) for word in self.ingredient_string.split() if Ingredient.objects.filter(name=word)!=[]][0]
		self.ingredient = ingredient

	def getResponseData(self):
		responseData = {}
		responseData["ingredient"] = str(self.ingredient)
		responseData["recipe"] = str(self.recipe)
		responseData["ingredient_string"] = self.ingredient_string
		responseData["available"] = self.available

		return responseData

	def isAvailable(self):
		return self.available

	def __unicode__(self):
		return "%s-%s"%(self.recipe, self.ingredient)

	def __str__(self):
		return "%s-%s"%(self.recipe, self.ingredient)

	def __hash__(self):
		return self.id

	def __cmp__(self, other):
		return self.id - other.id

	class Meta:
		ordering = ('recipe', 'ingredient')

