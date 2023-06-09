# Generated by Django 4.0.3 on 2023-03-18 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Material', '0001_initial'),
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripción')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=100, verbose_name='Telefono de Cliente')),
                ('prioridad', models.CharField(choices=[('N', 'Normal'), ('P', 'Prioritario')], default='N', max_length=1, verbose_name='Prioridad')),
                ('procesos', models.CharField(choices=[('SOLDADURA', 'Soldadura'), ('TORNO', 'Torno'), ('FRESADORA', 'Fresadora')], max_length=9, verbose_name='Procesos')),
                ('ubicacion', models.CharField(max_length=200, verbose_name='Ubicacion')),
                ('estado', models.CharField(choices=[('T', 'Terminada'), ('A', 'Archivada'), ('P', 'En Proceso')], max_length=1, verbose_name='Estado')),
                ('materiales', models.ManyToManyField(to='Material.material')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleados.empleado')),
            ],
        ),
    ]
