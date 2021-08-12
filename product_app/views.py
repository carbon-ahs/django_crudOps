from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

from .models import Product
from .forms import ProductForm

'''
from .models import 
from .forms import 
'''
app_name = 'product_app'

def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item has been added successfully!!')    
            redirect('home')

    form = ProductForm()
    
    product_fields = Product._meta.get_fields()
    contex = {
        'form': form,
        'key': 'value',
        'product_fields': product_fields,
    }
    return render(request, 'home.html', contex)



def about(request):
    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)

def tempu(request):
    header = 'TEMPU VRUMMMM'

    context = {
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
    }
    return render(request, 'tempu.html', context)


def product(request):
    header = 'All Products'
    try:
        all_product = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("No Model, Pls check migration.")    
    contex = {
        'all_product': all_product,
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
    }
    return render(request, 'product.html', contex)

def update(request, product_id):
    header = 'Update'

    if request.method == 'POST':
        product = Product.objects.get(pk = product_id)

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            
            messages.success(request, 'Item has been Edited successfully!!')
            return redirect('product')
    else:
        product = Product.objects.get(pk = product_id)
        form = ProductForm(instance=product)
        context = {
            'form': form,
            'header' : header,
            'key': 'value',
            'app_name' : app_name,
        }
        return render(request, 'update.html', context)


def delete(request, product_id):
    header = 'dlt'
    product = Product.objects.get(pk = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product')
    
    context = {
        'product': product,
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
    }
    return render(request, 'delete.html', context)

