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

def tops_view(request):
    return render(request, "aplicacion/tops.html")

def bottoms_view(request):
    return render(request, "aplicacion/bottoms.html")

def shoes_view(request):
    return render(request, "aplicacion/shoes.html")

def accessories_view(request):
    return render(request, "aplicacion/accessories.html")

def aboutme(request):
    return render(request, "aplicacion/aboutme.html")



#buscar producto
#def searchProduct(request):
    return render(request, "aplicacion/searchProduct.html")


#def search2(request):
    if request.GET['product']:
        product = request.GET['product']
        variabletops = tops.objects.filter(name__icontains=product)
        return render(request,
                      "aplicacion/resultsProduct.html",
                      {'product': product, "products": variabletops})
    return HttpResponse("No data to search!")





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
class TopsCreate(CreateView):
    model = tops
    fields = ['name', 'size', 'price', 'contact']
    success_url = reverse_lazy('tops')

class BottomsCreate(CreateView):
    model = bottoms
    fields = ['name', 'size', 'price', 'contact']
    success_url = reverse_lazy('bottoms')

class ShoesCreate(CreateView):
    model = shoes
    fields = ['name', 'size', 'price', 'contact']
    success_url = reverse_lazy('shoes')

class AccessoriesCreate(CreateView):
    model = accessories
    fields = ['name', 'size', 'price', 'contact']
    success_url = reverse_lazy('accessories')


#login
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            user = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user_2 = authenticate(username=user, password=password)
            if user_2 is not None:
                login(request, user)
                return render(request, "aplicacion/home.html", {"message": f"Welcome {user}"})
            else:
                return render(request, "aplicacion/login.html", {"form":miForm, "message": "Invalid data"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "message": "Invalid data"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})    


#register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():  
            user = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/home.html", {"mensaje":"Usuario Creado"})        
    else:
        form = UserRegisterForm() 

    return render(request, "aplicacion/register.html", {"form": form})   
