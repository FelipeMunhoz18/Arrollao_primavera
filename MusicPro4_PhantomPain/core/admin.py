from django.contrib import admin
from .models import Producto,Venta,Detalle,Rol,TipoProducto,ItemCarrito,Carrito

# Register your models here.

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Detalle)
admin.site.register(Rol)
admin.site.register(TipoProducto)
admin.site.register(ItemCarrito)
admin.site.register(Carrito)