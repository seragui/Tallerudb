# Generated by Django 4.0.3 on 2023-03-18 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ordentrabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordentrabajo',
            name='cliente',
            field=models.CharField(default='', max_length=100, verbose_name='Cliente'),
        ),
    ]
