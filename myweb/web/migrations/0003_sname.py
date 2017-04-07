# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_air_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_dj'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('personality', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=12, null=True)),
                ('photo', models.CharField(blank=True, max_length=15, null=True)),
                ('dateu', models.CharField(blank=True, db_column='dateU', max_length=30, null=True)),
            ],
            options={
                'db_table': 'sname',
                'managed': False,
            },
        ),
    ]
