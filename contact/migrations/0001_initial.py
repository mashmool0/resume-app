# Generated by Django 5.0.2 on 2024-03-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date', models.CharField(default='1402-12-17', max_length=20)),
            ],
        ),
    ]
