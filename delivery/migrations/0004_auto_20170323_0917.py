# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20170322_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='price',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]