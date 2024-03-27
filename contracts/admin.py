from django.contrib import admin
from .models import Contracts


@admin.register(Contracts)
class ContractsAdmin(admin.ModelAdmin):
    """
        list_display - отвечает за отображение полей в таблице
        list_display_links - отвечает за то какое поле является ссылкой
        ordering - отвечает за сортировку
        search_fields - по каким полям осуществляется поиск


    """
    #
    list_display = 'pk', 'name', 'cost',
    list_display_links = 'pk', 'name',
    ordering = 'pk',
    search_fields = 'name', 'product',
    date_hierarchy = 'start_data'
    list_filter = ('start_data',)




