from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import BusquedaForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

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