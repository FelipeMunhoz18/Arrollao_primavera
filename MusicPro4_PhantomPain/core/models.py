from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your models here.

#Tabla de roles
class Rol(models.Model):
    nombreRol= models.CharField(max_length=25,verbose_name='El nombre del rol de usuario')
    def __str__(self) -> str:
        return self.nombreRol

#Tabla de usuario
class Usuario(models.Model):
    #llave primaria
    nombreUsuario = models.CharField(max_length=25,verbose_name='El nombre que el usuario usa para ingresar a su cuenta')
    apellidos = models.CharField(max_length=25,verbose_name='El nombre que se mostrara algún día en la sección de comentarios')
    correoUsuario = models.CharField(max_length=25,verbose_name='El correo asociado a la cuenta')
    celular = models.IntegerField(verbose_name='El correo asociado a la cuenta')
    clave = models.CharField(max_length=25,verbose_name='El correo asociado a la cuenta')

    #llave foranea
    rol=models.ForeignKey(Rol,on_delete=models.PROTECT,verbose_name='La llave de rol-usuario')

    def __str__(self) -> str:
        return self.nombreUsuario

class TipoProducto(models.Model):
    nombreTipo= models.CharField(max_length=25,verbose_name='Nombre del tipo de producto')
    
    def __str__(self) -> str:
        return self.nombreTipo

#Tabla de modelos3d
class Producto(models.Model):
    #Llave primaria
    nombreProducto = models.CharField(max_length=400,verbose_name='El nombre asociado al producto')
    descripcionProducto = models.CharField(max_length=2000,verbose_name='La descripción asociada al producto en cuestión')
    precioProducto = models.IntegerField(verbose_name='El precio asociado al producto')
    stockProducto = models.IntegerField(verbose_name='El stock asociado al producto')
    imagenUno= models.ImageField(upload_to="CarpetaDestino",verbose_name='Primera imagen')
    imagenDos= models.ImageField(upload_to="CarpetaDestino",verbose_name='Segunda imagen', null=True)
    imagenTres= models.ImageField(upload_to="CarpetaDestino",verbose_name='Tercera imagen',null=True)
    imagenCuatro= models.ImageField(upload_to="CarpetaDestino",verbose_name='Cuarta imagen',null=True)
    tipoNombre=models.ForeignKey(TipoProducto,on_delete=models.PROTECT,verbose_name='La llave del tipo de producto',null=True)
    
    def __str__(self) -> str:
        return self.nombreProducto

#Tabla de ventas
class Venta(models.Model):
    #LLave primariaforanea
    #fecha
    fechaVenta = models.DateField()
    totalVenta= models.IntegerField(verbose_name='El total asociado a la venta despues de el iva de mierda')
    #Llave foranea
    nombreUsuario=models.ForeignKey(Usuario,on_delete=models.PROTECT,verbose_name='llave usuario-venta')

    def __str__(self) -> str:
        return self.fechaVenta

class Detalle(models.Model):
    #Llave primaria
    totalDetalle= models.IntegerField(verbose_name='El total asociado a la venta despues de el iva de mierda')
    #LLAVES foranea
    fechaVenta=models.ForeignKey(Venta,on_delete=models.PROTECT,verbose_name='llave Venta-Detalle')
    nombreProducto=models.ForeignKey(Producto,on_delete=models.PROTECT,verbose_name='llave Venta-Detalle')

class ItemCarrito(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    cantidad_actualizada = models.PositiveIntegerField(default=0)

    def subtotal(self):
        return self.producto.precioProducto * self.cantidad

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario', null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ESTADO_CHOICES = (
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    )
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierto')

def actualizar_cantidad(request):
    if request.method == 'POST' and request.is_ajax():
        product_id = request.POST.get('productId')
        quantity = request.POST.get('quantity')
        item = ItemCarrito.objects.get(pk=product_id)
        item.cantidad_actualizada = quantity
        item.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
