from django.contrib import admin
from car.models import CarModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at']
    search_fields = ['name']
    list_filter = ['create_at']