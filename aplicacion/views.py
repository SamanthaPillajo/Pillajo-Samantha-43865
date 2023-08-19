from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView


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
    ctx = {"tops": tops.objects.all()}
    return render(request, "aplicacion/tops.html", ctx)

@login_required
def bottoms_view(request):
    ctx = {"bottoms": bottoms.objects.all()}
    return render(request, "aplicacion/bottoms.html", ctx)

@login_required
def shoes_view(request):
    ctx = {"shoes": shoes.objects.all()}
    return render(request, "aplicacion/shoes.html", ctx)

@login_required
def accessories_view(request):
    ctx = {"accessories": accessories.objects.all()}
    return render(request, "aplicacion/accessories.html", ctx)

@login_required
def aboutme(request):
    return render(request, "aplicacion/aboutme.html")




#CRUD create
class TopsCreate(LoginRequiredMixin, CreateView):
    model = tops
    fields = '__all__'
    success_url = reverse_lazy('tops')

class BottomsCreate(LoginRequiredMixin, CreateView):
    model = bottoms
    fields = '__all__'
    success_url = reverse_lazy('bottoms')

class ShoesCreate(LoginRequiredMixin, CreateView):
    model = shoes
    fields = '__all__'
    success_url = reverse_lazy('shoes')
    
class AccessoriesCreate(LoginRequiredMixin, CreateView):
    model = accessories
    fields = '__all__'
    success_url = reverse_lazy('accessories')




#CRUD delete
class Topsdelete(LoginRequiredMixin, DeleteView):
    model = tops
    success_url = reverse_lazy('tops')  

class Bottomsdelete(LoginRequiredMixin, DeleteView):
    model = bottoms
    success_url = reverse_lazy('bottoms')  

class Shoesdelete(LoginRequiredMixin, DeleteView):
    model = shoes
    success_url = reverse_lazy('shoes')  

class Accessoriesdelete(LoginRequiredMixin, DeleteView):
    model = accessories
    success_url = reverse_lazy('accessories')  



#CRUD read
class TopsDetailView(LoginRequiredMixin, DetailView):
    model = tops  
    template_name = 'aplicacion/detail_top.html'  
    context_object_name = 'top' 

class BottomsDetailView(LoginRequiredMixin, DetailView):
    model = bottoms  
    template_name = 'aplicacion/detail_bottom.html'  
    context_object_name = 'bottom' 

class ShoesDetailView(LoginRequiredMixin, DetailView):
    model = shoes  
    template_name = 'aplicacion/detail_shoe.html'  
    context_object_name = 'shoe' 

class AccessoriesDetailView(LoginRequiredMixin, DetailView):
    model = accessories  
    template_name = 'aplicacion/detail_accessory.html'  
    context_object_name = 'accessory'



#CRUD update
class TopsUpdate(LoginRequiredMixin, UpdateView):
    model = tops
    fields = ['name', 'price', 'size', 'contact', 'photo']
    success_url = reverse_lazy('tops') 

class BottomsUpdate(LoginRequiredMixin, UpdateView):
    model = bottoms
    fields = ['name', 'price', 'size', 'contact', 'photo']
    success_url = reverse_lazy('bottoms') 

class ShoesUpdate(LoginRequiredMixin, UpdateView):
    model = shoes
    fields = ['name', 'price', 'size', 'contact', 'photo']
    success_url = reverse_lazy('shoes') 

class AccessoriesUpdate(LoginRequiredMixin, UpdateView):
    model = accessories
    fields = ['name', 'price', 'size', 'contact', 'photo']
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