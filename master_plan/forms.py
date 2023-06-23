from django import forms
from .models import WorkAxe, Activitie, Responsible, Date, MasterPlan

class WorkAxeForm(forms.Form):
    name = forms.CharField(label=('Eje de trabajo'))

class ActivitieForm(forms.Form):
    work_axe = forms.ModelChoiceField(label=('Eje de trabajo'), queryset=WorkAxe.objects.all())
    name = forms.CharField(label=('Nombre de Actividad'), widget=forms.Textarea)

class ResponsibleForm(forms.Form):
    name = forms.CharField(label=('Responsable')) 

class DateForm(forms.Form):
    class Meta:
        model = Date
        fields = '__all__'

class MasterPlanForm(forms.Form):
    name = forms.CharField(label='Master plan')
    description = forms.CharField(label='Descripción', widget=forms.Textarea)
    notes = forms.CharField(label='Notas', widget=forms.Textarea)

class DetailForm(forms.Form):
    master_plan = forms.ModelChoiceField(label=('Master plan'), queryset=MasterPlan.objects.all())
    activity = forms.ModelChoiceField(label=('Actividad'), queryset=Activitie.objects.all())
    responsible = forms.ModelChoiceField(label=('Responsable'), queryset=Responsible.objects.all())
    scheduled_date = forms.DateField(label=('Fecha a ejecutar'))
    completed_date = forms.DateField(label=('Fecha ejecutada'))
    evaluation = forms.CharField(label=('Evaluación'), widget=forms.Textarea, required=False)
    observations = forms.CharField(label=('Observaciones'), widget=forms.Textarea, required=False)