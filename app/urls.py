from django.urls import path,include
from .views import home_view,cart_view,contact_view,shop_view
urlpatterns=[
    path('',home_view,name='index'),
    path('cart/',cart_view,name='cart'),
    path('contact/',contact_view,name='contact'),
    path('shop/',shop_view,name='shop'),

]