# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-04 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ankieta', '0005_auto_20190804_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytanie',
            name='data_publikacji',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
