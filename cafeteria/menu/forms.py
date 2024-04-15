from django import forms
from .models import Producto, Orden

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'