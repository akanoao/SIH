# Generated by Django 5.1.1 on 2024-09-16 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SIHapp', '0009_bus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='route',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SIHapp.route'),
        ),
    ]
