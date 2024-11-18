from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User, EstructuraModel

class UserAdm(admin.ModelAdmin):
    pass
    """
    list_display = ['username', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']
    search_fields = ['username', 'first_name', 'last_name']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    """

class EstructuraModelAdm(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ftrab', 'ffirma', 'fnac', 'categoria', 'adsc_act', 'adsc_ant', 'turno', 'domicilio', 'colonia', 'municipio', 'seccional', 'num_cel', 'email', 'Resp_100', 'Resp_10', 'part_trab', 'inf_adic', 'descansos', 'vac_prog', 'servicio', 'promocion', 'movilizacion', 'asis_reu', 'voto_25Sept', 'engrupo', 'estatus', 'inf_admin', 'mi_resp', 'userId']
    search_fields = ['matricula']


admin.site.register(User, UserAdm)
admin.site.register(EstructuraModel, EstructuraModelAdm)