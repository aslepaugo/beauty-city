# Generated by Django 4.1.4 on 2022-12-11 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0011_saloon_master'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='saloon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Saloon', to='timetable.saloon', verbose_name='Салон'),
        ),
        migrations.AlterField(
            model_name='saloon',
            name='master',
            field=models.ManyToManyField(related_name='Saloons', to='timetable.master', verbose_name='Мастера в салоне'),
        ),
    ]