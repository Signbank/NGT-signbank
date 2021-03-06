# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0017_auto_20171208_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gloss',
            name='annotation_idgloss',
            field=models.CharField(help_text="\n    This is the Dutch name of a sign used by annotators when glossing the corpus in\nan ELAN annotation file. The Annotation Idgloss may be the same for two or\nmore entries (each with their own 'Sign Entry Name'). If two sign entries\nhave the same 'Annotation Idgloss' that means they differ in form in only\nminor or insignificant ways that can be ignored.", max_length=30, verbose_name='Annotation ID Gloss: Dutch'),
        ),
        migrations.AlterField(
            model_name='gloss',
            name='annotation_idgloss_en',
            field=models.CharField(blank=True, help_text="\n    This is the English name of a sign used by annotators when glossing the corpus in\nan ELAN annotation file. The Annotation Idgloss may be the same for two or\nmore entries (each with their own 'Sign Entry Name'). If two sign entries\nhave the same 'Annotation Idgloss' that means they differ in form in only\nminor or insignificant ways that can be ignored.", max_length=30, verbose_name='Annotation ID Gloss: English'),
        ),
    ]
