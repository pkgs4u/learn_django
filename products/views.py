from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import OrderedItems
from django.contrib import messages

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})
    # return  HttpResponse("<h1>Welcome</h1>");

def about(request):
    return HttpResponse("<h1>About Page</h1>")


def add_cart(request):
    if request.method=='POST':
        if request.POST.get('quantity'):
            savequantity = OrderedItems()
            savequantity.quantity = request.POST.get('quantity')
            savequantity.save()

            # savequantity = request.POST.get('quantity')
            # savequantity.save()
            messages.success(request, "Saved successfully")
            return  render(request, 'index.html')
    else:
        return render(request, 'index.html')

