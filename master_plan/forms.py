from django import forms
from django.forms.widgets import DateInput
from .models import WorkAxe, Activitie, Responsible, MasterPlan

class WorkAxeForm(forms.Form):
    name = forms.CharField(
        label=('Eje de trabajo'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })

class ActivitieForm(forms.Form):
    work_axe = forms.ModelChoiceField(
        label=('Eje de trabajo'), 
        queryset=WorkAxe.objects.all(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    name = forms.CharField(
        label=('Nombre de Actividad'), 
        widget=forms.Textarea,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })

class ResponsibleForm(forms.Form):
    name = forms.CharField(
        label=('Responsable'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        }) 

class MasterPlanForm(forms.Form):
    name = forms.CharField(
        label='Master plan',
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    description = forms.CharField(
        label='Descripción', 
        widget=forms.Textarea, 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    notes = forms.CharField(
        label='Notas', 
        widget=forms.Textarea, 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })

class DetailForm(forms.Form):
    master_plan = forms.ModelChoiceField(
        label=('Master plan'), 
        queryset=MasterPlan.objects.all(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    activity = forms.ModelChoiceField(
        label=('Actividad'), 
        queryset=Activitie.objects.all(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    responsible = forms.ModelChoiceField(
        label=('Responsable'), 
        queryset=Responsible.objects.all(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    scheduled_date = forms.DateField(
        label=('Fecha a ejecutar'), 
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    completed_date = forms.DateField(
        label=('Fecha ejecutada'), 
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    evaluation = forms.CharField(
        label=('Evaluación'), 
        widget=forms.Textarea, 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    observations = forms.CharField(
        label=('Observaciones'), 
        widget=forms.Textarea, 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })