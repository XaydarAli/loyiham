from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required()
def cart_view(request):
    return render(request,'cart.html')


@login_required()
def checkout_view(request):
    return render(request,'checkout.html')



def error_view(request):
    return render(request,'404.html')

def testimonial_view(request):
    return render(request,'testimonial.html')

