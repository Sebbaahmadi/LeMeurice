from django.shortcuts import render

# Create your views here.

def prod(request):
    return render(request, 'gallery//product.html')
