from django.contrib import admin
from .models import *

#--------------------------------------------- 
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ['id','descripCategoria'] 

admin.site.register(Categoria, CategoriaAdmin) 

#--------------------------------------------- 
class ProductoAdmin(admin.ModelAdmin): 
    list_display = ['nombre','descripcion', 'existencia'] 

admin.site.register(Producto, ProductoAdmin) 

#--------------------------------------------- 