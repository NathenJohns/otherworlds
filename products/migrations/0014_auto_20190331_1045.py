# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-31 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20190331_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_6',
            field=models.ImageField(blank=True, default='', upload_to='images'),
        ),
    ]