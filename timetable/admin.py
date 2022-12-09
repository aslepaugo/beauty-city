from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User, Master, Saloon, Service


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['telegram_id', 'fullname']


@admin.register(Master)
class Master(admin.ModelAdmin):
    list_display = (
        'fullname', 'speciality', 'saloon'
    )


@admin.register(Saloon)
class Saloon(admin.ModelAdmin):
    list_display = ['address']
    readonly_fields = ['lat', 'lon']


@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ['name', 'master', 'time', 'date', 'saloon']
