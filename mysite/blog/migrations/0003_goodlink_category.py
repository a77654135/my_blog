# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_goodlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodlink',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u94fe\u63a5\u5206\u7c7b'),
        ),
    ]
