# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 11:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20160913_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quserinfo',
            name='blood_pressure',
            field=models.FloatField(default=110.0, null=True, validators=[django.core.validators.MinValueValidator(70.0), django.core.validators.MaxValueValidator(210.0)]),
        ),
    ]
