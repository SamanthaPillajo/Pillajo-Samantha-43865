from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'aplicacion/home.html')

@login_required
def tops_view(request):
    ctx = {"top": tops.objects.all() }
    return render(request, "aplicacion/tops.html", ctx)


def bottoms_view(request):
    return render(request, "aplicacion/bottoms.html")

def shoes_view(request):
    return render(request, "aplicacion/shoes.html")

def accessories_view(request):
    return render(request, "aplicacion/accessories.html")

def aboutme(request):
    return render(request, "aplicacion/aboutme.html")



#search
@login_required
def busqueda_view(request):
    form = BusquedaForm(request.GET)
    resultados = []

    if form.is_valid():
        termino = form.cleaned_data['termino_busqueda']
        resultados += tops.objects.filter(name__icontains=termino)
        resultados += bottoms.objects.filter(name__icontains=termino)
        resultados += accessories.objects.filter(name__icontains=termino)
        resultados += shoes.objects.filter(name__icontains=termino)

    context = {
        'form': form,
        'resultados': resultados,
    }

    return render(request, 'aplicacion/busqueda.html', context)



#CRUD create
class TopsCreate(LoginRequiredMixin, CreateView):
    model = tops
    fields = ['name', 'size', 'price', 'contact', 'photo']
    success_url = reverse_lazy('tops')

class BottomsCreate(LoginRequiredMixin, CreateView):
    model = bottoms
    fields = ['name', 'size', 'price', 'contact', 'photo']
    success_url = reverse_lazy('bottoms')

class ShoesCreate(LoginRequiredMixin, CreateView):
    model = shoes
    fields = ['name', 'size', 'price', 'contact', 'photo']
    success_url = reverse_lazy('shoes')

class AccessoriesCreate(LoginRequiredMixin, CreateView):
    model = accessories
    fields = ['name', 'size', 'price', 'contact', 'photo']
    success_url = reverse_lazy('accessories')



#login
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(data=request.POST)
        if miForm.is_valid():
            user = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user_authenticated = authenticate(username=user, password=password)
            if user_authenticated is not None:
                login(request, user_authenticated)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).image.url
                except:
                    avatar = '/media/avatars/default.png'
                finally:
                    request.session['avatar'] = avatar
                return render(request, "aplicacion/home.html", {"message": f"Welcome {user}"})
            else:
                return render(request, "aplicacion/login.html", {"form": miForm, "message": "Invalid data"})
        else:
            return render(request, "aplicacion/login.html", {"form": miForm, "message": "Invalid data"})

    miForm = AuthenticationForm()
    return render(request, "aplicacion/login.html", {"form": miForm})



#register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():  
            user = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/home.html", {"message":"New user created"})        
    else:
        form = UserRegisterForm() 

    return render(request, "aplicacion/register.html", {"form": form})   



#edit user and avatar
@login_required
def EditUser(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data.get('email')
            user.password1 = form.cleaned_data.get('password1')
            user.password2 = form.cleaned_data.get('password2')
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            return render(request, "aplicacion/home.html", {'message': f"User {user.username} successfully updated"})
        else:
            return render(request, "aplicacion/edituser.html", {'form': form})
    else:
        form = UserEditForm(instance=user)
    return render(request, "aplicacion/edituser.html", {'form': form, 'usuario':user.username})


@login_required
def addAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
         
            oldavatar = Avatar.objects.filter(user=u)
            if len(oldavatar) > 0: 
                oldavatar[0].delete()

            #_________________ Grabo avatar nuevo
            avatar = Avatar(user=u, image=form.cleaned_data['image'])
            avatar.save()

            #_________________ Almacenar en session la url del avatar para mostrarla en base
            image = Avatar.objects.get(user=request.user.id).image.url
            request.session['avatar'] = image

            return render(request, "aplicacion/home.html")
    else:
        form = AvatarForm()
    return render(request, "aplicacion/addavatar.html", {'form': form})