from django.urls import path,include
from .views import  shop_detail_view
urlpatterns=[
    path('shop-detail', shop_detail_view, name='shop-detail'),


]