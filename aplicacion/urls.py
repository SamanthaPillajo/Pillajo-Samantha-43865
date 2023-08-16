from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index, name='home'),
    path('tops/', tops_view, name="tops" ),
    path('bottoms/', bottoms_view, name="bottoms" ),
    path('shoes/', shoes_view, name="shoes" ),
    path('accessories/', accessories_view, name="accessories" ),

    #path('searchProduct/', searchProduct, name="search_Product" ),
    #path('search2/', search2, name="search2" ),
    path('search/', busqueda_view, name="search" ),

    path('tops/', TopsCreate.as_view(), name="create_top" ), 
]