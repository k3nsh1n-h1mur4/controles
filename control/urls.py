from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.register, name='register'),
    path('list/', views.list, name='list'),
    path('details/<int:id>', views.details, name='details'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('export_excel/', views.export_excel, name='export_excel'),
    path('validate_matricula/', views.ValidateMatricula, name='validate_matricula'),
    path('validate_telefono/', views.ValidateTelefono, name='validate_telefono'),
    path('editar/<int:id>/', views.edit, name='edit'),
    path('save_edit/<int:id>/', views.save_edit, name='save_edit'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)