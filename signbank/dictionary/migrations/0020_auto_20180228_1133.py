# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0019_auto_20171221_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handshape',
            name='chinese_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Chinese name'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='dutch_name',
            field=models.CharField(max_length=50, verbose_name='Dutch name'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='english_name',
            field=models.CharField(max_length=50, verbose_name='English name'),
        ),
        migrations.AlterField(
            model_name='handshape',
            name='machine_value',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Machine value'),
        ),
    ]
