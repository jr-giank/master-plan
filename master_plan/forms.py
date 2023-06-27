from django import forms
from django.forms.widgets import DateInput
from .models import CustomUser, WorkAxe, Activitie, Responsible, MasterPlan, master_plan_status

class SignUpForm(forms.Form):
    
    first_name = forms.CharField(
        label=('Nombre'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    last_name = forms.CharField(
        label=('Apellido'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    email = forms.EmailField(
        label=('Correo'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
            'unique': 'El email ya esta asignado a otro usuario.'
        })
    password = forms.CharField(
        label=('Contraseña'),
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    password_confirmation = forms.CharField(
        label=('Confirmar contraseña'),
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })

class SignUpUpdateForm(forms.Form):

    first_name = forms.CharField(
        label=('Nombre'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    last_name = forms.CharField(
        label=('Apellido'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    email = forms.EmailField(
        label=('Correo'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
            'unique': 'El email ya esta asignado a otro usuario.'
        })
    password = forms.CharField(
        label=('Contraseña'),
        widget=forms.PasswordInput(),
        required=False,
        error_messages={
            'invalid': 'El valor ingresado es inválido.',
        })
    password_confirmation = forms.CharField(
        label=('Confirmar contraseña'),
        widget=forms.PasswordInput(),
        required=False,
        error_messages={
            'invalid': 'El valor ingresado es inválido.',
        })

class LoginForm(forms.Form):

    email = forms.EmailField(
        label=('Correo'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
            'unique': 'El email ya esta asignado a otro usuario.'
        })
    password = forms.CharField(
        label=('Contraseña'),
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })

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
    status = forms.ChoiceField(
        label='Estado', 
        choices=master_plan_status,
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
        queryset=CustomUser.objects.all(),
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