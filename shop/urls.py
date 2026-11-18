from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
path('privacy/', views.privacy, name='privacy'),
]