from django.db import models
import json, re
from django.urls import reverse # Used to generate URLs by reversing the URL patterns


# Create your models here.

class Chef(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50, unique=True)

	def getResponseData(self):
		responseData = {}
		responseData["chef_id"]=self.id
		responseData["first_name"]=self.first_name
		responseData["last_name"]=self.last_name
		responseData["email"]=self.email

		return responseData

	def __unicode__(self):
		return "%s %s"%(self.first_name,self.last_name)

	def __str__(self):
		return "%s %s"%(self.first_name,self.last_name)

	def __hash__(self):
		return self.id

	def __cmp__(self, other):
		return self.id - other.id

	# def get_absolute_url(self):
	# 	"""Returns the url to access a detail record for this user."""
	# 	return reverse('chef-detail', args=[str(self.id)])

	class Meta:
		ordering = ('first_name',)


class Ingredient(models.Model):
	name = models.CharField(max_length=50, unique=True)

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
	author = models.ForeignKey(Chef, on_delete=models.CASCADE)

	def getResponseData(self):
		responseData = {}
		responseData["ingredient_id"] = self.id
		responseData["title"] = self.title
		responseData["ingredients"] = self.ingredients
		responseData["directions"] = self.directions
		responseData["prep_time"] = self.prep_time
		responseData["cook_time"] = self.cook_time
		responseData["total_time"] = self.total_time
		responseData["serving_size"] = self.serving_size
		responseData["nutritional_info"] = self.nutritional_info
		responseData["thumbnail_url"] = self.thumbnail_url
		responseData["source"] = self.source
		responseData["author"] = self.author

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
	ingredient_string = models.CharField(max_length=50)

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


# class Quantity(models.Model):
# 	"""Quantities of Ingredients:
# 	eg. cup, tsp, tbsp, etc. 
# 	""" 
# 	name = models.CharField(max_length=50)

# 	def getResponseData(self):
# 		responseData = {}
# 		responseData["quantity_id"]=self.id
# 		responseData["name"]=self.name

# 		return responseData

# 	def __unicode__(self):
# 		return "%s"%(self.name)

# 	def __str__(self):
# 		return "%s"%(self.name)

# 	def __hash__(self):
#             	return self.id

# 	def __cmp__(self, other):
# 		return self.id - other.id

# 	class Meta:
# 		ordering = ('name',)

