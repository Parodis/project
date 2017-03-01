# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('city', models.CharField(max_length=100)),
                ('first_line_adress', models.CharField(max_length=255)),
                ('second_line_adress', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('personal_sale', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('forgot_key', models.CharField(max_length=255)),
            ],
        ),
    ]