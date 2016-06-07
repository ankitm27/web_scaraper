# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categary', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('domain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='intern.Domain')),
            ],
        ),
    ]
