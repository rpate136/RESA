from django.db import models
import json, re

# Create your models here.

class Chef(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

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

	class Meta:
		ordering = ('first_name',)

class Ingredient(models.Model):
	name = models.CharField(max_length=50)

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

