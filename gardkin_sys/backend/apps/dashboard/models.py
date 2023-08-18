from django.db import models

# Create your models here.
class states(models.Model):
    clave_estado = models.CharField(max_length=10, primary_key=True)
    nombre_estado = models.CharField(max_length=100)

class municipalities(models.Model):
    clave_municipio = models.CharField(max_length=10, primary_key=True)
    nombre_municipio = models.CharField(max_length=100)
    estado = models.ForeignKey('states', on_delete=models.DO_NOTHING)

class zones(models.Model):
    clave_zona = models.CharField(max_length=10, primary_key=True)
    nombre_zona = models.CharField(max_length=100)
    numero_zona = models.CharField(max_length=10)
    municipio = models.ForeignKey('municipalities', on_delete=models.DO_NOTHING)

class schools(models.Model):
    clave = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    turno = models.CharField(max_length=50)
    zona = models.ForeignKey('zones', on_delete=models.DO_NOTHING)
    director = models.ForeignKey('authentication.User', on_delete=models.DO_NOTHING, limit_choices_to={'tipo_usuario': 'Director/a', 'is_active': True})
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)

class groups(models.Model):
    grado = models.CharField(max_length=10)
    grupo = models.CharField(max_length=10)
    año = models.CharField(max_length=10)


class students(models.Model):
    curp = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    escuela = models.ForeignKey('schools', on_delete=models.DO_NOTHING)
    grupo = models.ForeignKey('groups', on_delete=models.DO_NOTHING)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)