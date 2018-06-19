# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-15 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_myproject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myproject',
            options={'ordering': ['-index', 'id'], 'verbose_name': '\u6211\u7684\u9879\u76ee', 'verbose_name_plural': '\u6211\u7684\u9879\u76ee'},
        ),
        migrations.AlterField(
            model_name='myproject',
            name='index',
            field=models.IntegerField(default=999, verbose_name='\u6392\u5e8f\uff08\u4ece\u5927\u5230\u5c0f\uff09'),
        ),
        migrations.AlterField(
            model_name='myproject',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='\u9879\u76ee\u5730\u5740'),
        ),
    ]