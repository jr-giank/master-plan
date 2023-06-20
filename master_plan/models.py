from django.db import models

class Work_axe(models.Model):

    """ Work axes model for the task """

    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name

class Activitie(models.Model):

    """ Activity model for the task """

    work_axe = models.ForeignKey(to=Work_axe, default="", on_delete=models.SET_DEFAULT)
    name = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.name

class Responsible(models.Model):
    
    """ Responsible model to say the responsible person for complete the task """
    
    name = models.CharField(max_length=75, null=False, blank=False)

    def __str__(self):
        return self.name

class Date(models.Model):

    """ Date model for the task """
        
    activitie = models.ForeignKey(to=Activitie, default="", on_delete=models.SET_DEFAULT)
    date = models.DateField(null=False, blank=False)
    responsible = models.ForeignKey(to=Responsible, default="", on_delete=models.SET_DEFAULT)
    date_made = models.DateField(null=True, blank=True)
    evaluation = models.CharField(max_length=75, null=True, blank=True)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.activitie.work_axe} - {self.activitie} - {self.date}"