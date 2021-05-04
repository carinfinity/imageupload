from django.contrib import admin
from .models import NewCar
# Register your models here.
@admin.register(NewCar)
class NewCarAdmin(admin.ModelAdmin):
    list_display = ('id', 'carname', 'cardesc', 'carimage')