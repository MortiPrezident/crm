from django.contrib import admin
from .models import Leads

@admin.register(Leads)
class LeadsAdmin(admin.ModelAdmin):
    """
        list_display - отвечает за отображение полей в таблице
        list_display_links - отвечает за то какое поле является ссылкой
        ordering - отвечает за сортировку
        search_fields - по каким полям осуществляется поиск


    """
    #
    list_display = 'pk', 'first_name', 'last_name', 'phone', 'email'
    list_display_links = 'pk', 'first_name', 'last_name'
    ordering = 'pk',
    search_fields = 'first_name', 'last_name', 'phone', 'email', 'ad',


