from django.contrib import admin

# Register your models here.
from .models import Categoria, Contatos


class ContatoAdmin (admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'datacriacao', 'categoria', 'ativo')
    list_display_links = ('nome', 'sobrenome')
    #list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'ativo')


admin.site.register(Categoria)
admin.site.register(Contatos, ContatoAdmin)
