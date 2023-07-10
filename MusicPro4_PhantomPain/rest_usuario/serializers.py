from rest_framework import serializers
from core.models import Usuario,Producto
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario','apellidos','correoUsuario','celular','clave','rol']
        

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombreProducto','descripcionProducto','precioProducto','stockProducto','imagenUno','imagenDos','imagenTres','imagenCuatro','tipoNombre']