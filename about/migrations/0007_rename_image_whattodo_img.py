# Generated by Django 5.0.2 on 2024-03-04 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_alter_whattodo_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whattodo',
            old_name='image',
            new_name='img',
        ),
    ]
