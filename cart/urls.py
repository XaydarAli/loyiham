from django.urls import path,include
from .views import error_view,checkout_view,cart_view,testimonial_view
urlpatterns=[
    path('error/',error_view,name='404'),
    path('cart/',cart_view,name='cart'),
    path('testimonial/',testimonial_view,name='testimonial'),
    path('checkout/',checkout_view,name='checkout'),

]