from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product_list/', Productlist.as_view(), name='product_list'),
    path('<id>/<slug>/', product_detail, name='product_detail'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),


]