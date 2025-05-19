from django.contrib import admin

from .models import Training

@admin.register(Training)
class TrainingAdminSnow(admin.ModelAdmin):
    list_display = ('date', 'description', 'is_completed')
