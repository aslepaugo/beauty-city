from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User, Master, Saloon, Service, ServiceType


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['telegram_id', 'fullname']


@admin.register(Master)
class Master(admin.ModelAdmin):
    list_display = (
        'fullname', 'speciality',
    )


@admin.register(Saloon)
class Saloon(admin.ModelAdmin):
    list_display = ['title', 'address']
    readonly_fields = ['lat', 'lon']


@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ['name', 'time', 'date', 'saloon']

@admin.register(ServiceType)
class ServiceType(admin.ModelAdmin):
    list_display = ['name']
