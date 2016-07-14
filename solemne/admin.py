from django.contrib import admin
from solemne.models import Marcas, Categorias, Productos

# Register your models here.

class MarcasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen', 'created_at', 'updated_at')

class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre','orden_de_la_categoria','status','created_at','updated_at')
    #list_filter = ('owner','active')
    search_fields = ('nombre',)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('sku','nombre','precio','marca','categoria','status','created_at','updated_at',)
    search_fields = ('nombre',)

admin.site.register(Productos, ProductosAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Marcas, MarcasAdmin)
