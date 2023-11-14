from django.db import models

# Create your models here.
from django.db import models

class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key=True)
    edad = models.IntegerField(default=0)
    genero = models.BooleanField(default=False)
    fecha_realizacion = models.DateField(null=True, blank=True)
    tipos_lenguajes = models.TextField(null=True, blank=True)
    años_programacion = models.IntegerField(default=0)
    areas_especialidad = models.TextField(null=True, blank=True)
    marco_trabajo = models.TextField(null=True, blank=True)
    sistemas_operativos = models.TextField(null=True, blank=True)
    tipos_proyectos = models.TextField(null=True, blank=True)
    herramientas_comunicacion = models.TextField(null=True, blank=True)
    herramientas_desarrollo = models.TextField(null=True, blank=True)

    class Meta:
        # Comenta la línea db_table si quieres seguir la convención de nombres predeterminada
        db_table = "perfil"
