from django.db import models

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

class Responsible(models.Model):
    
    """ Responsible model to say the responsible person for complete the task """
    
    name = models.CharField(max_length=75, null=False, blank=False, verbose_name='Nombre')

    def __str__(self):
        return self.name

class Date(models.Model):

    """ Date model for the task """
        
    activitie = models.ForeignKey(to=Activitie, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(null=False, blank=False)
    responsible = models.ForeignKey(to=Responsible, null=True, blank=True, on_delete=models.SET_NULL)
    date_made = models.DateField(null=True, blank=True)
    evaluation = models.CharField(max_length=75, null=True, blank=True)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.activitie.work_axe} - {self.activitie} - {self.date}"

class MasterPlan(models.Model):

    """ Master plan model for a project """

    name = models.CharField(max_length=75, null=False, blank=False, verbose_name='Nombre')
    description = models.TextField(null=True, blank=True, verbose_name='Descripción')
    date_created = models.DateField(auto_now_add=True, verbose_name='Fecha creación')
    notes = models.TextField(null=True, blank=True, verbose_name='Notas')

    def __str__(self):
        return f"{self.name}"

class Detail(models.Model):

    """ Detail model for an entire project info """

    master_plan = models.ForeignKey(to=MasterPlan, on_delete=models.CASCADE, verbose_name='Master plan')
    work_axe = models.ForeignKey(to=WorkAxe, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Eje de trabajo')
    activity = models.ForeignKey(to=Activitie, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Actividad')
    responsible = models.ForeignKey(to=Responsible, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Responsable')
    scheduled_date = models.DateField(null=False, blank=False, verbose_name='Fecha programada')
    completed_date = models.DateField(null=False, blank=False, verbose_name='Fecha completada')
    evaluation = models.TextField(null=True, blank=True, verbose_name='Evaluación')
    observations = models.TextField(null=False, blank=False, verbose_name='Observaciones')

    def __str__(self):

        return f'{self.master_plan} - {self.activity}'