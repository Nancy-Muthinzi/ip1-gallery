# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20180925_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='gallery.tags'),
        ),
    ]