# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-29 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190329_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_6',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
