# Generated by Django 5.1.1 on 2024-09-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIHapp', '0005_alter_busstop_route'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busstop',
            name='route',
        ),
        migrations.AddField(
            model_name='route',
            name='bus_stop',
            field=models.ManyToManyField(blank=True, to='SIHapp.busstop'),
        ),
    ]
