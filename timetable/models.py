from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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


class Master(models.Model):
    fullname = models.CharField(
        max_length=100,
        help_text='Введите имя и фамилию мастера',
        verbose_name='Имя и фамилия мастера'
    )
    telegram_id = models.IntegerField(
        verbose_name='Телеграм-ID мастера'
    )
    speciality = models.CharField(
        max_length=1000,
        help_text='Введите специальность',
        verbose_name='Специальность мастера',
    )
    saloon = models.CharField(
        max_length=1000,
        help_text='Салон в котором работает мастер',
        verbose_name='Салон',
    )

    class Meta:
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


class Saloon(models.Model):
    CHOICES = (
        (0, 'Парикмахерские услуги'),
        (1, 'Ногтевой сервис'),
        (2, 'Макияж'),
    )
    address = models.CharField(
        'Адрес салона',
        help_text='Адрес где находится салон',
        max_length=200,
    )
    masters = models.ForeignKey(
        to=Master,
        on_delete=models.CASCADE,
        related_name='saloons',
        verbose_name='Мастер',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'


class Service(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название услуги',
    )
    price = models.IntegerField(
        verbose_name='Цена услуги'
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

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
