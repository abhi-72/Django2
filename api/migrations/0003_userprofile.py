# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180913_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('D', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=45)),
                ('display_name', models.CharField(max_length=45)),
                ('upd_on', models.DateTimeField()),
                ('mobile', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
