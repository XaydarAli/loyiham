from django.shortcuts import render
from shop.models import Product, Category
from django.contrib.auth.decorators import  login_required

def home_view(request):
    if request.method=="POST":
        search=request.POST['search']
        products=Product.objects.filter(name__icontains=search)
        return render(request,'shop.html',{'products':products})
    categories=Category.objects.all()
    products=Product.objects.all()
    context={
        'categories':categories,
        'products':products,
    }
    return render(request,'index.html',context)



def shop_view(request):
    if request.method == 'POST':
            search = request.POST["search"]
            product = Product.objects.filter(name__icontains=search)
            return render(request, 'shop.html', {'product': product})
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
def shop_detail_view(request):
    def shop_detail(request, slug):
        categories = Category.objects.get(slug=slug)
        return render(request, 'shop-detail.html', {'categories': categories})
@login_required()
def contact_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Product.objects.filter(name__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'contact.html', context)


@login_required()
def cart_view(request):
    if request.method == "POST":
        search = request.POST['search']
        products = Product.objects.filter(name__icontains=search)
        return render(request, 'shop.html', {'products': products})
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        "categories": categories,
        "products": products,
    }
    return render(request, 'cart.html', context)




