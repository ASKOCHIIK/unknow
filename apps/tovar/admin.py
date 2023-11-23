from django.contrib import admin
from .models import *


class TovarImageInlines(admin.TabularInline):
    model = TovarImage
    extra = 1


@admin.register(Tovar)
class TovarAdmin(admin.ModelAdmin):
    inlines = [TovarImageInlines]
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title']
