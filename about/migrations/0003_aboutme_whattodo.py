# Generated by Django 5.0.2 on 2024-03-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_headerinfo_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WhatToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
