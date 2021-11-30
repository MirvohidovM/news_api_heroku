from django.contrib import admin
from .models import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "photo", "created_at", "views", "featured")
    list_filter = ("featured", "created_at")
    search_fields = ("title",)


admin.site.register(Category)