from django.shortcuts import render
from .models import Producto, Orden
from .forms import ProductoForm, OrdenForm

def menu(request):
    productos = Producto.objects.all()
    return render(request, 'menu/menu.html', {'productos': productos})

def pedido(request):
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrdenForm()
    return render(request, 'menu/pedido.html', {'form': form})

def buscar(request):
    if 'q' in request.GET:
        q = request.GET['q']
        productos = Producto.objects.filter(nombre__icontains=q)
    else:
        productos = Producto.objects.none()
    return render(request, 'menu/buscar.html', {'productos': productos})