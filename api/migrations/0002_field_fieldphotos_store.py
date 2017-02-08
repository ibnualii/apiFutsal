# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-02-08 03:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id_field', models.AutoField(primary_key=True, serialize=False)),
                ('name_field', models.CharField(max_length=30)),
                ('latitude_field', models.FloatField()),
                ('longitude_field', models.FloatField()),
                ('description_field', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'field',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id_store', models.AutoField(primary_key=True, serialize=False)),
                ('name_store', models.CharField(max_length=40)),
                ('description_store', models.CharField(max_length=100)),
                ('contact_store', models.CharField(max_length=14)),
                ('link_store', models.CharField(max_length=40)),
                ('photo_store', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FieldPhotos',
            fields=[
                ('id_field', models.ForeignKey(db_column='id_field', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.Field')),
                ('field_photos', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'field_photos',
                'managed': False,
            },
        ),
    ]