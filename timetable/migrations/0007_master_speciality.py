# Generated by Django 4.1.4 on 2022-12-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_remove_master_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='speciality',
            field=models.CharField(choices=[('US', 'United States'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy')], default='', max_length=1000),
            preserve_default=False,
        ),
    ]
