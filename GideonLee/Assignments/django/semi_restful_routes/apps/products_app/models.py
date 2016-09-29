from __future__ import unicode_literals
from django.db import models

class ProductManager(models.Manager):
	def validate_new(self, **kwargs):
		try:
			price = float(kwargs['price'])
			Product.objects.create(name=kwargs['name'], description=kwargs['description'], price=price)
			return (True, 'Success')
		except:
			return (False, 'Error: Price must be a number.')
	def validate_update(self, **kwargs):
		try: 
			price = float(kwargs['price'])
			product = Product.objects.get(id=kwargs['id'])
			product.name = kwargs['name']
			product.description = kwargs['description']
			product.price = price
			product.save()
		except:
			return (False, 'Error: New price must be a valid number.')

class Product(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField(max_length=1000)
	price = models.FloatField()
	objects = ProductManager()