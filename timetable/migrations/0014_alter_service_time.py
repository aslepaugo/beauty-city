# Generated by Django 4.1.4 on 2022-12-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0013_remove_master_telegram_id_remove_service_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='time',
            field=models.CharField(choices=[('1', '8.00-9.45'), ('2', '10.00-11.45'), ('3', '12.00-13.45'), ('4', '14.00-15.45'), ('5', '16.00-17.45'), ('6', '18.00-19.45')], help_text='Время записи', max_length=200, verbose_name='Время записи'),
        ),
    ]
