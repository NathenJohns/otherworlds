# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-31 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190331_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_4',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_5',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_6',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
