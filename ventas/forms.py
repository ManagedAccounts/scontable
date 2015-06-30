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

