# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_profile_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='type',
        ),
    ]
