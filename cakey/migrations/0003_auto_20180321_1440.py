# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakey', '0002_remove_post_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('caption', models.CharField(max_length=500)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cakey.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='cake',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cake',
        ),
        migrations.DeleteModel(
            name='Cake',
        ),
        migrations.AddField(
            model_name='post',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cakey.Recipe'),
        ),
    ]
