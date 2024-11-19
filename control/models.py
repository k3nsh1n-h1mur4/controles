from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import UserManager, PermissionsMixin

from django.contrib.auth.base_user import AbstractBaseUser


def create_user_receiver(sender, instance, created, **kwargs):
    pass 

post_save.connect(create_user_receiver, sender=settings.AUTH_USER_MODEL)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = 'username'
    email = models.EmailField(max_length=100, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    
    REQUIRED_FIELDS = ['is_superuser', 'is_staff', 'is_active', 'email']

    objects = UserManager()

class EstructuraModel(models.Model):
    class Meta:
        db_table = 'estructuratbl'
        
    matricula = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100, null=True)
    ftrab = models.CharField(max_length=250, null=True)
    ffirma = models.CharField(max_length=250, null=True)
    fnac = models.CharField(max_length=30, null=True)
    categoria = models.CharField(max_length=100, null=True)
    adsc_act = models.CharField(max_length=100, null=True)
    adsc_ant = models.CharField(max_length=100, null=True)
    turno = models.CharField(max_length=100, null=True)
    domicilio = models.CharField(max_length=150, null=True)
    colonia = models.CharField(max_length=100, null=True)
    municipio = models.CharField(max_length=100, null=True)
    seccional = models.CharField(max_length=10, null=True)
    num_cel = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=100, null=True)
    Resp_100 = models.CharField(max_length=100, null=True)
    Resp_10 = models.CharField(max_length=100, null=True)
    part_trab = models.CharField(max_length=250, null=True)
    inf_adic = models.CharField(max_length=250, null=True)
    descansos = models.CharField(max_length=50, null=True)
    vac_prog = models.CharField(max_length=150, null=True)
    servicio = models.CharField(max_length=150, null=True)
    promocion = models.CharField(max_length=150, null=True)
    movilizacion = models.CharField(max_length=150, null=True)
    asis_reu = models.CharField(max_length=150, null=True)
    voto_25Sept = models.CharField(max_length=150, null=True)
    engrupo = models.CharField(max_length=150, null=True)
    estatus = models.CharField(max_length=150, null=True)
    inf_admin = models.CharField(max_length=250, null=True)
    mi_resp = models.CharField(max_length=100, null=True)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)