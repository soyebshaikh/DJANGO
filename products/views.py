#from django.shortcuts import render, HttpResponse

# Create your views here.
#def index(request):
   # return render(request,'index.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
 products = Product.objects.all()
 return render(request, 'index.html', {'products': products})
 # return HttpResponse("<h1> Welcome to Django Project </h1>")
