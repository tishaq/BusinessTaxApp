# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-20 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_app', '0002_auto_20191020_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='supervisor',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]