from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    list_display - отвечает за отображение полей в таблице
    list_display_links - отвечает за то какое поле является ссылкой
    ordering - отвечает за сортировку
    search_fields - по каким полям осуществляется поиск


    """

    #
    list_display = (
        "pk",
        "lead",
    )
    list_display_links = "pk", "lead"
    ordering = ("pk",)
    search_fields = "lead__first_name", "contract__name"
