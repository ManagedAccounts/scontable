<<<<<<< HEAD
from django import forms
from .models import Cliente, Producto, CategoriaProducto
from django.forms import ModelForm


class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=['ruc','razon_social','direccion','telefono']

class ProductoForm(ModelForm):
    class Meta:
        model=Producto
        fields=['code','number','categoria','nombre','descripcion','imagen','precio','afecto','stock','estado']
        exclude=['igv']
=======
# coding:utf-8
from django.forms import ModelForm
from ventas.models import Comprobante, Cliente, Detalle

class ComprobanteForm(ModelForm):
     class Meta:
         model = Comprobante
         fields = ['cliente', 'tabla_10', 'serie', 'numero', 'fecha', 'igv', 'total']
         # exclude = ['']

class ClienteForm(ModelForm):
     class Meta:
         model = Cliente
         fields = ['ruc', 'razon_social', 'direccion']

class DetalleForm(ModelForm):
     class Meta:
         model = Detalle
         fields = ['comprobante', 'cantidad', 'articulo', 'importe']
>>>>>>> fe03928482c4e52e1d5e6bd71d0ee9253f8b703d

class CategoriaForm(ModelForm):
    class Meta:
        model=CategoriaProducto
        fields=['nombre','descripcion']
