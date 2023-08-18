from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, no_trabajador, nombre, apellido_paterno, apellido_materno, email, password, tipo_usuario):
        if not no_trabajador:
            raise ValueError('El usuario debe tener un numero de trabajador')
        user = self.model(
            no_trabajador=no_trabajador,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            email=self.normalize_email(email),
            tipo_usuario=tipo_usuario
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, no_trabajador, nombre, apellido_paterno, apellido_materno, email, password,
                         tipo_usuario):
        user = self.create_user(
            no_trabajador=no_trabajador,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            email=self.normalize_email(email),
            password=password,
            tipo_usuario=tipo_usuario
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

tipo_usuario = [
    ('Administrador', 'Administrador'),
    ('Director/a', 'Director/a'),
    ('Maestro/a', 'Maestro/a'),
]

class User(AbstractBaseUser):
    no_trabajador = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    tipo_usuario = models.CharField(max_length=50, choices=tipo_usuario)
    escuela = models.ForeignKey('dashboard.schools', on_delete=models.DO_NOTHING, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'no_trabajador'
    REQUIRED_FIELDS = ['nombre', 'apellido_paterno', 'apellido_materno', 'email', 'tipo_usuario']

    def __str__(self):
        return self.no_trabajador
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        verbose_name_plural = 'Usuarios'
        verbose_name = 'Usuario'
        ordering = ['no_trabajador']


