from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    edad = models.IntegerField(default=0)
    genero = models.TextField(null=True,blank=True)
    fecha_realizacion = models.DateField(default=timezone.now,null=True, blank=True)
    tipos_lenguajes = models.TextField(null=True, blank=True)
    años_programacion = models.IntegerField(default=0)
    areas_especialidad = models.TextField(null=True, blank=True)
    marco_trabajo = models.TextField(null=True, blank=True)
    frame_works = models.TextField(null=True, blank=True)
    sistemas_operativos = models.TextField(null=True, blank=True)
    online_community = models.TextField(null=True, blank=True)
    challenge_devs = models.TextField(null=True, blank=True)
    herramientas_comunicacion = models.TextField(null=True, blank=True)
    herramientas_desarrollo = models.TextField(null=True, blank=True)
    curriculum_link = models.TextField(null=True, blank=True)

    class Meta:
        # Comenta la línea db_table si quieres seguir la convención de nombres predeterminada
        db_table = "perfil"
class Validar(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    validacion = models.BooleanField(default=True)
    class Meta:
        db_table='validar'