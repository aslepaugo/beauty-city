from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .utils.geo_helper import get_lat_lon


class ServiceType(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Услуга',
        help_text='Введите тип услуги'
    )
    price = models.IntegerField(
        verbose_name='Цена услуги'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Типы услуг'


class Saloon(models.Model):
    title = models.CharField(
        'Имя салона',
        max_length=256
    )
    address = models.CharField(
        'Адрес салона',
        help_text='Адрес где находится салон',
        max_length=200,
    )

    lat = models.FloatField(default=None, blank=True, null=True)
    lon = models.FloatField(default=None, blank=True, null=True)
    master = models.ManyToManyField(
        'Master',
        verbose_name='Мастера в салоне',
        related_name='Saloons'
    )

    def save(self, *args, **kwargs):
        self.lat, self.lon = get_lat_lon(self.address)
        super(Saloon, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}, {self.address}'

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Master(models.Model):
    fullname = models.CharField(
        max_length=100,
        help_text='Введите имя и фамилию мастера',
        verbose_name='Имя и фамилия мастера'
    )
    speciality = models.ForeignKey(
        to=ServiceType,
        related_name='Services',
        on_delete=models.CASCADE,
        help_text='Введите специальность',
        verbose_name='Специальность мастера',
    )
    saloon = models.ForeignKey(
        to=Saloon,
        on_delete=models.CASCADE,
        related_name='Saloon',
        verbose_name='Салон',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.fullname}, {self.speciality}'


class User(models.Model):
    telegram_id = models.IntegerField(
        verbose_name='Телеграм-ID клиента'
    )
    fullname = models.CharField(
        max_length=100,
        help_text='Введите имя и фамилию клиента',
        verbose_name='Имя и фамилия клиента'
    )
    phone_number = PhoneNumberField(
        'Номер клиента', blank=True, max_length=20
    )

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



class Service(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название услуги',
    )
    CHOICES = (
        ('Payed', 'Оплачен'),
        ('Done', 'Выполнен'),
        ('Cancel', 'Отменен'),
    )
    status = models.CharField(
        max_length=200,
        choices=CHOICES
    )
    date = models.DateField(
        help_text='Дата записи',
        verbose_name='Дата записи',
    )
    time = models.TimeField(
        help_text='Время записи',
        verbose_name='Время записи'
    )
    master = models.ForeignKey(
        to=Master,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='Мастер',
    )
    saloon = models.ForeignKey(
        to=Saloon,
        on_delete=models.CASCADE,
        verbose_name='Салон'
    )


    def __str__(self):
        return f'{self.name}, {self.status}, {self.saloon}, {self.date}, {self.master}, {self.time}'


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
