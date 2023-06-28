from django.db import models
from django.contrib.auth.models import AbstractUser

user_roles = [
    ('A', 'admin'),
    ('B', 'responsable')
]

master_plan_status = [
    ('A', 'Activo'),
    ('B', 'Cerrado')
]

detail_status = [
    ('A', 'No Completado'),
    ('B', 'Completado')
]

class CustomUser(AbstractUser):

    """ User custom model for authentication process in the application """
    
    first_name = models.CharField(max_length=70, null=False, blank=False, verbose_name='Nombre')
    last_name = models.CharField(max_length=70, null=False, blank=False, verbose_name='Apellido')
    username = models.CharField(max_length=70, unique=False, blank=True, null=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name='Correo')
    role = models.CharField(max_length=5, choices=user_roles, default='A', verbose_name='Rol')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password', 'role']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class WorkAxe(models.Model):

    """ Work axes model for the task """

    name = models.CharField(max_length=75, null=False, blank=False, verbose_name='Nombre')

    def __str__(self):
        return self.name

class Activitie(models.Model):

    """ Activity model for the task """

    work_axe = models.ForeignKey(to=WorkAxe, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Eje de trabajo')
    name = models.TextField(null=False, blank=False, verbose_name='Nombre')
    
    def __str__(self):
        return self.name

class MasterPlan(models.Model):

    """ Master plan model for a project """

    name = models.CharField(max_length=75, null=False, blank=False, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    date_created = models.DateField(auto_now_add=True, verbose_name='Fecha creación')
    status = models.CharField(max_length=7, choices=master_plan_status, default='A', verbose_name='Estado')
    notes = models.TextField(null=True, blank=True, verbose_name='Notas')

    def __str__(self):
        return f"{self.name}"

class Detail(models.Model):

    """ Detail model for an entire project info """

    master_plan = models.ForeignKey(to=MasterPlan, on_delete=models.CASCADE, verbose_name='Master plan')
    work_axe = models.ForeignKey(to=WorkAxe, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Eje de trabajo')
    activity = models.ForeignKey(to=Activitie, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Actividad')
    responsible = models.ForeignKey(to=CustomUser, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Responsable')
    status = models.CharField(max_length=13, choices=detail_status, default='A', verbose_name='Estado')
    scheduled_date = models.DateField(null=False, blank=False, verbose_name='Fecha programada')
    completed_date = models.DateField(null=True, blank=True, verbose_name='Fecha completada')
    evaluation = models.TextField(null=True, blank=True, verbose_name='Evaluación')
    observations = models.TextField(null=False, blank=False, verbose_name='Observaciones')

    def __str__(self):

        return f'{self.master_plan} - {self.activity}'