# Generated by Django 5.0.2 on 2024-03-04 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_remove_whattodo_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='whattodo',
            name='img',
            field=models.ImageField(default=True, upload_to='media/'),
        ),
    ]