# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 09:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cakey', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]
