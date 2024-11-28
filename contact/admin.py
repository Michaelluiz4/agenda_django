from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',    # nomes do display
    ordering = '-id', # ordenação da lista (estou ordenando em ordem descrecente pelo id por ex, mas poderia usar outro meio de ordenação)
    list_filter = 'date',  # criar um filtro, estou criando um filtro de data por ex
    search_fields = 'id', 'first_name', 'last_name', # campo de busca
    list_per_page = 10 # itens que aparecerão por página
    list_max_show_all = 200 # limite máximo de itens por página
    list_editable = 'show',
    # list_editable = 'first_name',
    list_display_links = 'id', 'first_name' # onde fica o link estou colocando no id e first_name por ex


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',