from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    list_display - отвечает за отображение полей в таблице
    list_display_links - отвечает за то какое поле является ссылкой
    ordering - отвечает за сортировку
    search_fields - по каким полям осуществляется поиск


    """

    #
    list_display = "pk", "name", "description_short", "price"
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = ("name",)
    change_list_template = "accounts/admin/profile_change_list.html"

    def description_short(self, obj: Product) -> str:
        if len(obj.description) > 30:
            return obj.description[:30] + "..."

        return obj.description
