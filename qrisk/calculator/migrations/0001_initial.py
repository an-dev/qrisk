# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 15:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=30, validators=[django.core.validators.MinValueValidator(25), django.core.validators.MaxValueValidator(84)])),
                ('sex', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], default='M', max_length=10)),
                ('ethnicity', models.CharField(choices=[('WHITE', 'WHITE'), ('INDIAN', 'INDIAN'), ('PAKISTANI', 'PAKISTANI'), ('BANGLADESHI', 'BANGLADESHI'), ('ASIAN', 'ASIAN'), ('BLACK_CAR', 'BLACK_CAR'), ('BLACK_AFR', 'BLACK_AFR'), ('CHINESE', 'CHINESE'), ('OTHER', 'OTHER')], default='WHITE', max_length=25)),
                ('postcode', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QUserInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='calculator.QUser')),
                ('smoking_status', models.CharField(choices=[('NON-SMOKER', 'NON-SMOKER'), ('EX-SMOKER', 'EX-SMOKER'), ('LIGHT-SMOKER', 'LIGHT-SMOKER'), ('MOD-SMOKER', 'MOD-SMOKER'), ('HEAVY-SMOKER', 'HEAVY-SMOKER')], default='NON-SMOKER', max_length=25)),
                ('diabetes_status', models.CharField(choices=[('', 'NONE'), ('T1', 'T1'), ('T2', 'T2')], default='', max_length=5)),
                ('heart_attacked_relative', models.BooleanField(default=False, verbose_name='Angina or heart attack in a 1st degree relative < 60')),
                ('kidney_disease', models.BooleanField(default=False, verbose_name='Chronic kidney disease (stage 4 or 5)')),
                ('atrial_fibrillation', models.BooleanField(default=False)),
                ('blood_pressure_treat', models.BooleanField(default=False)),
                ('rheumatoid_arthritis', models.BooleanField(default=False)),
                ('cholesterol_hdl_ratio', models.DecimalField(decimal_places=1, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(12.0)])),
                ('blood_pressure', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(70), django.core.validators.MaxValueValidator(210)])),
                ('height', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(140), django.core.validators.MaxValueValidator(210)])),
                ('weight', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(40), django.core.validators.MaxValueValidator(180)])),
            ],
        ),
    ]
