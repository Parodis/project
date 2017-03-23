# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 21:13
from __future__ import unicode_literals

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20170306_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Maximum file size allowed is 5Mb', null=True, upload_to='dist/img', validators=[category.models.validate_image]),
        ),
    ]
