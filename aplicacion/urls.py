from django.contrib import admin
from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index, name='home'),
    path('tops/', tops_view, name="tops"),
    path('bottoms/', bottoms_view, name="bottoms" ),
    path('shoes/', shoes_view, name="shoes" ),
    path('accessories/', accessories_view, name="accessories" ),
    path('aboutme/', aboutme, name="aboutme" ),

    #path('searchProduct/', searchProduct, name="search_Product" ),
    #path('search2/', search2, name="search2" ),
    path('search/', busqueda_view, name="search" ),

    path('tops_form/', TopsCreate.as_view(), name="create_top" ), 
    path('bottoms_form/', BottomsCreate.as_view(), name="create_bottom" ), 
    path('shoes_form/', ShoesCreate.as_view(), name="create_shoe" ), 
    path('accessories_form/', AccessoriesCreate.as_view(), name="create_accessory" ), 


    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),


]