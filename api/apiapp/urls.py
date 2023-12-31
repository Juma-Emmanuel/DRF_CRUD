from django.contrib import admin
from django.urls import path
from . import views
from .views import *
app_name = "apiapp"
urlpatterns = [
          
           path('products/', views.product_list),
           path('products/<int:id>', views.product_detail)

]