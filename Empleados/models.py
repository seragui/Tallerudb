from django.db import models

# Create your models here.


class Cargo(models.Model):

    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(
        'Nombre de Cargo', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = ("Cargo")
        verbose_name_plural = ("Cargos")

    def __str__(self):
        return self.nombre_cargo


class Departamento(models.Model):

    id_departamento=models.AutoField(primary_key=True)
    nombre_departamento = models.CharField(
        'Nombre de Departamento', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = ('Departamento')
        verbose_name_plural = ('Departamentos')

    def __str__(self):
        return self.nombre_departamento

class Empleado(models.Model):
    idempleado= models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre',max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    dui = models.CharField('DUI', max_length=10, blank=False,null=False)
    sexo = models.CharField('Sexo', max_length=1, blank=False, null=False)
    email = models.CharField('email',max_length=100,blank=False, null=False)
    estadoCivil = models.CharField('estadoCivil', max_length=10, blank=False,null=False)
    telefono = models.CharField('Telefono', max_length=9 ,blank=False,null=False)
    fechaNaci = models.DateField('Fecha de Nacimiento',blank=False,null=False)
    direccion = models.TextField('Direccion',max_length=300, blank=False,null=False)
    id_cargo = models.ForeignKey(
        'Cargo', verbose_name='Cargo', on_delete=models.CASCADE, blank=False )
    id_departamento = models.ForeignKey(
        'Departamento', verbose_name='Departamento', on_delete=models.CASCADE, blank=False )
    
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural= 'Empleados'
        ordering=['idempleado']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellidos