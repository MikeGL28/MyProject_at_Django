from django.contrib import admin
from .models import Hobby

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'internal_url')
    prepopulated_fields = {'slug': ('name',)}