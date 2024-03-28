from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Админка для профиля

    list_display - отвечает за отображение полей в таблице
    list_display_links - отвечает за то какое поле является ссылкой
    ordering - отвечает за сортировку
    search_fields - по каким полям осуществляется поиск

    get_queryset - сокращает количество запросов к БД
    """

    #
    list_display = "pk", "user", "position", "avatar"
    list_display_links = "pk", "user"
    ordering = ("pk",)
    search_fields = ("user__username",)
    change_list_template = "accounts/admin/profile_change_list.html"

    def get_queryset(self, request):
        return Profile.objects.select_related("user")
