# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-09 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='what_did_you_eat_today',
            field=models.CharField(default='', max_length=200),
        ),
    ]
