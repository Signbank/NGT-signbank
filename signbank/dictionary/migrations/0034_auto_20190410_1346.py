# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-10 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0033_auto_20190403_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldchoice',
            options={'ordering': ['machine_value']},
        ),
        migrations.AlterModelOptions(
            name='lemmaidgloss',
            options={'ordering': ['dataset__acronym']},
        ),
        migrations.AlterField(
            model_name='dataset',
            name='exclude_choices',
            field=models.ManyToManyField(blank=True, help_text='Exclude these field choices', to='dictionary.FieldChoice'),
        ),
        migrations.AlterField(
            model_name='othermedia',
            name='type',
            field=models.CharField(choices=[('0', '-'), ('1', 'N/A'), ('2', 'Alternative citation form'), ('3', 'Citation form with mouthing'), ('11', 'Elicitation image'), ('10', 'Handy signs: experiments (mouthing, long)'), ('5', 'Handy signs: experiments (mouthing, short)'), ('8', 'Handy signs: experiments (no mouthing, long)'), ('9', 'Handy signs: experiments (no mouthing, short)'), ('4', 'Sign in sentence context'), ('6', 'SignPhon: citation form'), ('7', 'SignPhon: sentence')], max_length=5),
        ),
    ]
