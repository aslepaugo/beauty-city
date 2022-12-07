from django.db import models


class User(models.Model):
    telegram_id = models.IntegerField(
        verbose_name='Телеграм-ID клиента'
    )
    fullname = models.CharField(
        max_length=100,
        help_text='Введите имя и фамилию клиента',
        verbose_name='Имя и фамилия клиента'
    )
    phone_number = models.PhoneNumberField(
        'Номер клиента', blank=True, max_length=20
    )

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Клиенты'
