# Generated by Django 4.0.3 on 2023-03-18 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Material', '0003_alter_material_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='imagen',
        ),
    ]