# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-31 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190331_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_main',
            new_name='image_1',
        ),
    ]
