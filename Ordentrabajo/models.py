from django.db import models
from Empleados.models import Empleado
from Material.models import Material

# Create your models here.

class OrdenTrabajo(models.Model):
    prio_choices=(('N','Normal'),('P','Prioritario'))
    procesos_choices=(('SOLDADURA','Soldadura'),('TORNO','Torno'),('FRESADORA','Fresadora'))
    estado_choices=(('T','Terminada'),('A','Archivada'),('P','En Proceso'))

    id_orden=models.AutoField(primary_key="True")
    cliente=models.CharField('Cliente',max_length=100,blank=False, null=False, default="")
    #proveedor=models.CharField('Proveedores', max_length='')
    descripcion=models.TextField('Descripción',max_length=100, blank=False, null=False)
    correo= models.EmailField('Correo',max_length=100, blank=False, null=False)
    telefono=models.CharField('Telefono de Cliente',max_length=100, blank=False, null=False)
    vendedor=models.ForeignKey(Empleado,on_delete=models.CASCADE, blank=False)
    materiales=models.ManyToManyField(Material)
    prioridad=models.CharField('Prioridad',max_length=1,choices=prio_choices, default='N',blank=False, null=False)
    procesos=models.CharField('Procesos',max_length=9,choices=procesos_choices, blank=False, null=False)
    ubicacion=models.CharField('Ubicacion', max_length=200, blank=False, null=False)
    estado=models.CharField('Estado',max_length=1, choices=estado_choices,blank=False, null=False )
