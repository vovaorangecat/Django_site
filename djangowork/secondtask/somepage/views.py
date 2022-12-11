from django.shortcuts import render
from somepage.models import ProductCategory, Product
# Create your views here.

def createone(request):
    context = {
        'title': 'Test Title',

               }
    return render(request,'somepage/createone.html', context)

def createtwo(request):
    context = {
        'title': 'Store-каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'somepage/createtwo.html', context)
