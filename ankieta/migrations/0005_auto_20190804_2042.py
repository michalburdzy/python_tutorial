# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-04 20:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankieta', '0004_auto_20190804_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytanie',
            name='data_publikacji',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
