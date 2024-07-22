from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from .models import Product,Category
from django.contrib.auth.decorators import  login_required
def shop_view(request):
    if request.method == 'POST':
            search = request.POST["search"]
            product = Product.objects.filter(name__icontains=search)
            return render(request, 'shop.html', {'product': product})
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
def shop_detail_view(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'shop-detail.html',context)











