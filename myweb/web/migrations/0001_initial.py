# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotelsdj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, null=True)),
                ('hotel', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hotelsdj',
                'managed': False,
            },
        ),
    ]
