# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170301_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='order_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
