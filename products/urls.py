from django.urls import path
from .views import products_view, product_create_view, product_details_view

urlpatterns = [
    path("", products_view, name="products"),                        #/product/
    path("create/", product_create_view, name="product_create"),     #/product/create
    path("<int:id>/", product_details_view, name="product_details")  #/product/5
]