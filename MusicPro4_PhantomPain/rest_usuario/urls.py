from django.urls import path
from rest_usuario.views import lista_usuarios,lista_producto

urlpatterns=[
    path('lista_usuarios',lista_usuarios, name='lista_usuarios'),
    path('lista_producto',lista_producto, name='lista_producto')
 ]
