from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, SignUpUpdateForm, LoginForm, WorkAxeForm, ActivitieForm, ResponsibleForm, MasterPlanForm, DetailForm, FilterForm
from .models import CustomUser, WorkAxe, Activitie, Responsible, MasterPlan, Detail, master_plan_status

from .functions import is_admin 
import datetime
import re

# Authentication
def SignUpView(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if form.is_valid():
            if password != password_confirmation:
                form.add_error('password', 'Las contraseñas no coinciden.')
                
                return render(request=request, template_name='create.html', context={'form': form})

            user = CustomUser.objects.create()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.password = make_password(password)
            user.save()

            return redirect('master-plan')
    else:
        form = SignUpForm()

    return render(request=request, template_name='create.html', context={'form': form})

def LoginView(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('master-plan')
            else:
                form.add_error('password', 'Credenciales inválidas')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def LogoutView(request):
    logout(request)

    return redirect('login')

# Main views
@login_required
def MasterDetailView(request, pk):
    if request.method == 'GET':
        form = FilterForm()
        
        master = MasterPlan.objects.get(id=pk)
        master_names = MasterPlan._meta.fields

        # Normal
        excluded_fields = ['master_plan']

        records_name = [field for field in Detail._meta.fields if field.name not in excluded_fields]
        
        if is_admin(request.user) == True:
            records = Detail.objects.filter(master_plan=master.id)
        else:
            records = Detail.objects.filter(master_plan=master.id, responsible=request.user.id)
    
    if request.method == 'POST':
        form = FilterForm(request.POST)

        master = MasterPlan.objects.get(id=pk)
        master_names = MasterPlan._meta.fields

        # Normal
        excluded_fields = ['master_plan']

        records_name = [field for field in Detail._meta.fields if field.name not in excluded_fields]
        
        if is_admin(request.user) == True:
            records = Detail.objects.filter(master_plan=master.id)
        else:
            records = Detail.objects.filter(master_plan=master.id, responsible=request.user.id)
        
        if form.is_valid():
            action = request.POST.get('action')
            
            if action == 'search':
                # Filters
                work_axe = form.cleaned_data['work_axe']
                activity = form.cleaned_data['activity']
                responsible = form.cleaned_data['responsible']
                scheduled_date = form.cleaned_data['scheduled_date']
                completed_date = form.cleaned_data['completed_date']

                if work_axe:
                    records = records.filter(work_axe=work_axe)
                if activity:
                    records = records.filter(activity=activity)
                if responsible:
                    records = records.filter(responsible=responsible)
                if scheduled_date:
                    records = records.filter(scheduled_date=scheduled_date)
                if completed_date:
                    records = records.filter(completed_date=completed_date)

                form = FilterForm(initial={'work_axe':work_axe, 'activity':activity, 'responsible':responsible, 'scheduled_date':scheduled_date, 'completed_date':completed_date})

            return render(request=request, template_name='master-detail.html', context={'master':master, 'master-names':master_names, 'records':records, 'records_name':records_name, 'form':form}) 
    return render(request=request, template_name='master-detail.html', context={'master':master, 'master-names':master_names, 'records':records, 'records_name':records_name, 'form':form})

@login_required
# WorkAxe Logic Views
def ListWorkAxeView(request):

    records = WorkAxe.objects.all()
    records_name = WorkAxe._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

@login_required
def CreateWorkAxeView(request):

    if request.method == 'POST':
        form = WorkAxeForm(request.POST)

        if form.is_valid():
            work_axe = WorkAxe.objects.create()
            work_axe.name = request.POST['name']
            work_axe.save()

            return redirect('work-axe')
    else:
        form = WorkAxeForm()

    return render(request=request, template_name='create.html', context={'form': form})

@login_required
def UpdateWorkAxeView(request, pk):

    work_axe = WorkAxe.objects.get(id=pk)
    
    if request.method == 'POST':
        form = WorkAxeForm(request.POST)

        if form.is_valid():
            work_axe.name = request.POST['name']
            work_axe.save()

            return redirect('work-axe')
    else:
        form = WorkAxeForm(initial={'name':work_axe.name})

    return render(request=request, template_name='update.html', context={'form': form})

@login_required
def DeleteWorkAxeView(request, pk):

    record = WorkAxe.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('work-axe')

    return render(request=request, template_name='delete.html')

# Activity Logic Views
@login_required
def ListActivityView(request):

    records = Activitie.objects.all()
    records_name = Activitie._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

@login_required
def CreateActivityView(request):

    if request.method == 'POST':
        form = ActivitieForm(request.POST)

        if form.is_valid():
            work_axe = WorkAxe.objects.get(id=request.POST['work_axe'])
            activity = Activitie.objects.create(work_axe=work_axe, name=request.POST['name'])
            
            return redirect('activity')
    else:
        form = ActivitieForm()

    return render(request=request, template_name='create.html', context={'form': form})

@login_required
def UpdateActivityView(request, pk):

    activity = Activitie.objects.get(id=pk)
    
    if request.method == 'POST':
        form = ActivitieForm(request.POST)

        if form.is_valid():
            work_axe = WorkAxe.objects.get(id=request.POST['work_axe'])

            activity.work_axe = work_axe
            activity.name = request.POST['name']
            activity.save()

            return redirect('activity')
    else:
        form = ActivitieForm(initial={'work_axe':activity.work_axe, 'name':activity.name})

    return render(request=request, template_name='update.html', context={'form': form})

@login_required
def DeleteActivityView(request, pk):

    record = Activitie.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('activity')

    return render(request=request, template_name='delete.html')

# Responsible Logic Views
@login_required
def ListResponsibleView(request):

    records = CustomUser.objects.all()
    records_name = CustomUser._meta.fields

    excluded_fields = ['is_staff', 'is_active', 'is_superuser', 'date_joined', 'last_login', 'password', 'username', 'role']

    records = CustomUser.objects.all()
    records_name = [field for field in CustomUser._meta.fields if field.name not in excluded_fields]

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

@login_required
def CreateResponsibleView(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
    
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if form.is_valid():
            if password != password_confirmation:
                form.add_error('password', 'Las contraseñas no coinciden.')
                
                return render(request=request, template_name='create.html', context={'form': form})

            responsible = CustomUser.objects.create()
            responsible.first_name = request.POST['first_name']
            responsible.last_name = request.POST['last_name']
            responsible.email = request.POST['email']
            responsible.role = 'B'
            responsible.password = make_password(password)
            responsible.save()

            return redirect('responsible')
    else:
        form = SignUpForm()

    return render(request=request, template_name='create.html', context={'form': form})

@login_required
def UpdateResponsibleView(request, pk):

    responsible = CustomUser.objects.get(id=pk)
    
    if request.method == 'POST':
        form = SignUpUpdateForm(request.POST)

        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if form.is_valid():
            if password_confirmation != None and password != None and password != password_confirmation:
                form.add_error('password', 'Las contraseñas no coinciden.')
                
                return render(request=request, template_name='create.html', context={'form': form})

            if password != None:
                responsible.password = make_password(password)

            responsible.first_name = request.POST['first_name']
            responsible.last_name = request.POST['last_name']
            responsible.email = request.POST['email']
            responsible.save()

            return redirect('responsible')
    else:
        form = SignUpUpdateForm(initial={
            'first_name':responsible.first_name,
            'last_name': responsible.last_name,
            'email': responsible.email,
            })

    return render(request=request, template_name='update.html', context={'form': form})

@login_required
def DeleteResponsibleView(request, pk):

    record = CustomUser.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('responsible')

    return render(request=request, template_name='delete.html')

# MasterPlan Logic Views
@login_required
def ListMasterPlanView(request):

    records = MasterPlan.objects.all()
    records_name = MasterPlan._meta.fields

    for instance in records:
        instance.status = dict(master_plan_status)[instance.status]

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

@login_required
def CreateMasterPlanView(request):

    if request.method == 'POST':
        form = MasterPlanForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.create()
            master_plan.name = request.POST['name']
            master_plan.description = request.POST['description']
            master_plan.notes = request.POST['notes']
            master_plan.save()

            return redirect('master-plan')
    else:
        form = MasterPlanForm()

    return render(request=request, template_name='create.html', context={'form': form})

@login_required
def UpdateMasterPlanView(request, pk):

    master_plan = MasterPlan.objects.get(id=pk)
    
    if request.method == 'POST':
        form = MasterPlanForm(request.POST)

        if form.is_valid():
            master_plan.name = request.POST['name']
            master_plan.description = request.POST['description']
            master_plan.status = request.POST['status']
            master_plan.notes = request.POST['notes']
            master_plan.save()

            return redirect('master-plan')
    else:
        form = MasterPlanForm(initial={
            'name':master_plan.name,
            'description':master_plan.description,
            'status':master_plan.status,
            'notes':master_plan.notes
            })

    return render(request=request, template_name='update.html', context={'form': form})

@login_required
def DeleteMasterPlanView(request, pk):

    record = MasterPlan.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('master-plan')

    return render(request=request, template_name='delete.html')

# Detail Logic Views
@login_required
def ListDetailView(request):

    records = Detail.objects.all()
    records_name = Detail._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

@login_required
def CreateDetailView(request):

    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = CustomUser.objects.get(id=request.POST['responsible'])
            complete_date = request.POST['completed_date']
            
            if complete_date == '':
                complete_date = None
            
            detail = Detail.objects.create(
                master_plan=master_plan,
                work_axe=work_axe,
                activity=activity,
                responsible=responsible,
                scheduled_date=request.POST['scheduled_date'],
                completed_date=complete_date,
                evaluation = request.POST['evaluation'],
                observations = request.POST['observations']
            )

            return redirect('detail')
    else:
        form = DetailForm()

    return render(request=request, template_name='create.html', context={'form': form})

@login_required
def CreateMasterDetailView(request, pk):

    master = MasterPlan.objects.get(id=pk)

    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = CustomUser.objects.get(id=request.POST['responsible'])
            complete_date = request.POST['completed_date']
            
            if complete_date == '':
                complete_date = None
            
            detail = Detail.objects.create(
                master_plan=master_plan,
                work_axe=work_axe,
                activity=activity,
                responsible=responsible,
                scheduled_date=request.POST['scheduled_date'],
                completed_date=complete_date,
                evaluation = request.POST['evaluation'],
                observations = request.POST['observations']
            )
            url_actual = request.build_absolute_uri()

            nueva_url = re.sub(f'/detail/create/{pk}/', '', url_actual)
            
            nueva_url += f'/master/plan/details/{pk}/'

            return redirect(nueva_url)
    else:
        form = DetailForm(initial={
            'master_plan':master.id
        })

    return render(request=request, template_name='create.html', context={'form': form})

@login_required
def UpdateDetailView(request, pk):

    detail = Detail.objects.get(id=pk)
    
    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = CustomUser.objects.get(id=request.POST['responsible'])
            complete_date = request.POST['completed_date']
            
            if complete_date == '':
                complete_date = None

            detail.master_plan=master_plan
            detail.work_axe=work_axe
            detail.activity=activity
            detail.responsible=responsible
            detail.scheduled_date = request.POST['scheduled_date']
            detail.completed_date = complete_date
            detail.evaluation = request.POST['evaluation']
            detail.observations = request.POST['observations']
            detail.save()

            return redirect('detail')
    else:
        try:
            complete_date = detail.completed_date.strftime('%Y-%m-%d'),
        except AttributeError:
            complete_date = datetime.datetime.now().strftime('%Y-%m-%d')
        form = DetailForm(initial={
            'master_plan':detail.master_plan,
            'work_axe':detail.work_axe,
            'activity':detail.activity,
            'responsible':detail.responsible,
            'scheduled_date':detail.scheduled_date.strftime('%Y-%m-%d'),
            'evaluation':detail.evaluation,
            'observations':detail.observations
            })

    return render(request=request, template_name='update.html', context={'form': form})

@login_required
def DeleteDetailView(request, pk):

    record = Detail.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('detail')

    return render(request=request, template_name='delete.html')