from django import forms
from django.forms.widgets import DateInput
from .models import CustomUser, Component, Activitie, MasterPlan, master_plan_status, detail_status

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

class ComponentForm(forms.Form):
    name = forms.CharField(
        label=('Componente'),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
            'unique': 'Este componente ya existe.'
        })

class ActivitieForm(forms.Form):
    component = forms.ModelChoiceField(
        label=('Componente'), 
        queryset=Component.objects.all(),
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
            'unique': 'Esta actividad ya existe.'
        })

class MasterPlanForm(forms.Form):
    name = forms.CharField(
        label='Master plan',
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
            'unique': 'Este master plan ya existe.'
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
    goal_manager = forms.ModelChoiceField(
        label=('Gerente de objetivo'), 
        queryset=CustomUser.objects.all(),
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    activity_manager = forms.ModelChoiceField(
        label=('Responsable actividad'), 
        queryset=CustomUser.objects.all(),
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    supervision_manager = forms.ModelChoiceField(
        label=('Responsable supervisión'), 
        queryset=CustomUser.objects.all(),
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    expected_results = forms.CharField(
        label=('Resultado esperado'), 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
    })
    objectives = forms.CharField(
        label=('Objectivos'), 
        widget=forms.Textarea, 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
    })
    goal = forms.CharField(
        label=('Meta'), 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
    })
    tasks = forms.CharField(
        label=('Tareas'), 
        widget=forms.Textarea, 
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
    })
    status = forms.ChoiceField(
        label='Estado', 
        choices=detail_status,
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
    quantities = forms.IntegerField(
        label='Cantidades',
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
    })
    unit_cost = forms.DecimalField(
        max_digits=10, 
        decimal_places=2,
        label='Costo Unitario', 
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

class FilterForm(forms.Form):

    component = forms.ModelChoiceField(
        label=('Componente'),
        queryset=Component.objects.all(),
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    activity = forms.ModelChoiceField(
        label=('Actividad'), 
        queryset=Activitie.objects.all(),
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    responsible = forms.ModelChoiceField(
        label=('Responsable'), 
        queryset=CustomUser.objects.all(),
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    status = forms.ChoiceField(
        label='Estado', 
        choices=detail_status,
        required=False,
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    scheduled_date = forms.DateField(
        label=('Fecha programada'), 
        required=False,
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })
    completed_date = forms.DateField(
        label=('Fecha completada'), 
        required=False,
        widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
        error_messages={
            'required': 'Este campo es requerido.',
            'invalid': 'El valor ingresado es inválido.',
        })