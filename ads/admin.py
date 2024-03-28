from django.contrib import admin
from ads.models import Ads


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    """
    list_display - отвечает за отображение полей в таблице
    list_display_links - отвечает за то какое поле является ссылкой
    ordering - отвечает за сортировку
    search_fields - по каким полям осуществляется поиск

    get_queryset - сокращает количество запросов к БД

    """

    #
    list_display = "pk", "name", "budget", "product"
    list_display_links = "pk", "name"
    ordering = ("pk",)
    search_fields = ("name",)
    change_list_template = "accounts/admin/profile_change_list.html"
