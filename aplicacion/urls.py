from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='inicio'),
    path('tops/', tops, name="tops" ),
    path('bottoms/', bottoms, name="bottoms" ),
    path('shoes/', shoes, name="shoes" ),
    path('accesories/', accesories, name="accesories" ),
]