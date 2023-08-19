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


#CRUD create
    path('tops_form/', TopsCreate.as_view(), name="create_top" ), 
    path('bottoms_form/', BottomsCreate.as_view(), name="create_bottom" ), 
    path('shoes_form/', ShoesCreate.as_view(), name="create_shoe" ), 
    path('accessories_form/', AccessoriesCreate.as_view(), name="create_accessory" ), 



#CRUD delete
path('delete_top/<int:pk>/', Topsdelete.as_view(), name="delete_top"),
path('delete_bottom/<int:pk>/', Bottomsdelete.as_view(), name="delete_bottom"),
path('delete_shoe/<int:pk>/', Shoesdelete.as_view(), name="delete_shoe"),
path('delete_accessory/<int:pk>/', Accessoriesdelete.as_view(), name="delete_accessory"),


#CRUD detail
path('detail_top/<int:pk>/', TopsDetailView.as_view(), name="detail_top"),
path('detail_bottom/<int:pk>/', BottomsDetailView.as_view(), name="detail_bottom"),
path('detail_shoe/<int:pk>/', ShoesDetailView.as_view(), name="detail_shoe"),
path('detail_accessory/<int:pk>/', AccessoriesDetailView.as_view(), name="detail_accessory"),



#CRUD update
 path('update_top/<int:pk>/', TopsUpdate.as_view(), name="update_top"),
 path('update_bottom/<int:pk>/', BottomsUpdate.as_view(), name="update_bottom"),
 path('update_shoe/<int:pk>/', ShoesUpdate.as_view(), name="update_shoe"),
 path('update_accessory/<int:pk>/', AccessoriesUpdate.as_view(), name="update_accessory"),


#Login Logout and Register
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),

#Edit User
    path('edit_user/', EditUser, name="edit_user"),
    path('add_avatar/', addAvatar, name="add_avatar"),
]