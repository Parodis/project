# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20170322_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
