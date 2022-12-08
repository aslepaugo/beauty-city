from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import User, Master, Saloon


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
