from django import forms
from .models import Work_axe, Activitie, Responsible, Date

class WorkAxeForm(forms.Form):
    name = forms.CharField(label=('Eje de trabajo'))

class ActivitieForm(forms.Form):
    class Meta:
        model = Activitie
        fields = '__all__'

class ResponsibleForm(forms.Form):
    name = forms.CharField(label=('Eje de trabajo')) 

class DateForm(forms.Form):
    class Meta:
        model = Date
        fields = '__all__'