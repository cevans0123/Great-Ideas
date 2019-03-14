# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-26 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('great_ideas', '0002_auto_20180726_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=700)),
                ('description', models.TextField(max_length=255)),
                ('location', models.TextField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('posted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to='great_ideas.User')),
            ],
        ),
        migrations.CreateModel(
            name='Myjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=700)),
                ('description', models.TextField(max_length=255)),
                ('location', models.TextField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worked_by', to='great_ideas.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='idea',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='idea',
            name='posted',
        ),
        migrations.DeleteModel(
            name='Idea',
        ),
    ]