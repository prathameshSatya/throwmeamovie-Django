# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.CharField(max_length=40)),
                ('imdbID', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('imdbRating', models.CharField(max_length=4)),
                ('tomatoeRating', models.CharField(max_length=4)),
                ('genre1', models.CharField(max_length=20)),
                ('genre2', models.CharField(max_length=20)),
                ('genre3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.CharField(max_length=40)),
                ('friends_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('expPreference1', models.CharField(max_length=20)),
                ('expPreference2', models.CharField(max_length=20)),
                ('derPreference1', models.CharField(max_length=20)),
                ('derPreference2', models.CharField(max_length=20)),
            ],
        ),
    ]
