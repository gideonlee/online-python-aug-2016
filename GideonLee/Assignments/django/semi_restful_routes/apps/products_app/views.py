from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product
from django.contrib import messages

# Create your views here.
def index(request):
	all_products = Product.objects.all()
	context = {
		'products': all_products
	}
	return render(request, 'products_app/index.html', context)

def show(request, id):
	product = Product.objects.get(id=id)
	context = {
		'product': product
	}
	return render(request, 'products_app/show.html', context)

def new(request):
	return render(request, 'products_app/new.html')

def create(request):
	result = Product.objects.validate_new(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	if not result[0]: 
		messages.error(request, result[1])
		return redirect(reverse('products:new'))
	return redirect(reverse('products:index'))

def edit(request, id):
	product = Product.objects.get(id=id)
	context = {
		'product': product
	}
	return render(request, 'products_app/edit.html', context)

def update(request, id):
	result = Product.objects.validate_update(id=id, name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	return redirect(reverse('products:index'))

def destroy(request, id):
	Product.objects.get(id=id).delete()
	return redirect(reverse('products:index'))