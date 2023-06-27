from django.shortcuts import render, redirect, resolve_url
from .forms import WorkAxeForm, ActivitieForm, ResponsibleForm, MasterPlanForm, DetailForm
from .models import WorkAxe, Activitie, Responsible, MasterPlan, Detail
import datetime
import re

# Main views
def HomeView(request):

    records = MasterPlan.objects.values('id', 'name', 'date_created')
    
    return render(request=request, template_name='home.html', context={'records': records})

def MasterDetailView(request, pk):

    excluded_fields = ['master_plan']

    master = MasterPlan.objects.get(id=pk)
    master_names = MasterPlan._meta.fields

    records = Detail.objects.filter(master_plan=master.id)
    records_name = [field for field in Detail._meta.fields if field.name not in excluded_fields]
    
    return render(request=request, template_name='master-detail.html', context={'master':master, 'master-names':master_names, 'records':records, 'records_name':records_name})

# WorkAxe Logic Views
def ListWorkAxeView(request):

    records = WorkAxe.objects.all()
    records_name = WorkAxe._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

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

def DeleteWorkAxeView(request, pk):

    record = WorkAxe.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('work-axe')

    return render(request=request, template_name='delete.html')

# Activity Logic Views
def ListActivityView(request):

    records = Activitie.objects.all()
    records_name = Activitie._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

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

def DeleteActivityView(request, pk):

    record = Activitie.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('activity')

    return render(request=request, template_name='delete.html')

# Responsible Logic Views
def ListResponsibleView(request):

    records = Responsible.objects.all()
    records_name =Responsible._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

def CreateResponsibleView(request):

    if request.method == 'POST':
        form = ResponsibleForm(request.POST)

        if form.is_valid():
            responsible = Responsible.objects.create()
            responsible.name = request.POST['name']
            responsible.save()

            return redirect('responsible')
    else:
        form = ResponsibleForm()

    return render(request=request, template_name='create.html', context={'form': form})

def UpdateResponsibleView(request, pk):

    responsible = Responsible.objects.get(id=pk)
    
    if request.method == 'POST':
        form = ResponsibleForm(request.POST)

        if form.is_valid():
            responsible.name = request.POST['name']
            responsible.save()

            return redirect('responsible')
    else:
        form = ResponsibleForm(initial={'name':responsible.name})

    return render(request=request, template_name='update.html', context={'form': form})

def DeleteResponsibleView(request, pk):

    record = Responsible.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('responsible')

    return render(request=request, template_name='delete.html')

# MasterPlan Logic Views
def ListMasterPlanView(request):

    records = MasterPlan.objects.all()
    records_name = MasterPlan._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

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

def UpdateMasterPlanView(request, pk):

    master_plan = MasterPlan.objects.get(id=pk)
    
    if request.method == 'POST':
        form = MasterPlanForm(request.POST)

        if form.is_valid():
            master_plan.name = request.POST['name']
            master_plan.description = request.POST['description']
            master_plan.notes = request.POST['notes']
            master_plan.save()

            return redirect('master-plan')
    else:
        form = MasterPlanForm(initial={
            'name':master_plan.name,
            'description':master_plan.description,
            'notes':master_plan.notes
            })

    return render(request=request, template_name='update.html', context={'form': form})

def DeleteMasterPlanView(request, pk):

    record = MasterPlan.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('master-plan')

    return render(request=request, template_name='delete.html')

# Detail Logic Views
def ListDetailView(request):

    records = Detail.objects.all()
    records_name = Detail._meta.fields

    return render(request=request, template_name='list.html', context={'records': records, 'records_name': records_name})

def CreateDetailView(request):

    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = Responsible.objects.get(id=request.POST['responsible'])
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

def CreateMasterDetailView(request, pk):

    master = MasterPlan.objects.get(id=pk)

    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = Responsible.objects.get(id=request.POST['responsible'])
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

def UpdateDetailView(request, pk):

    detail = Detail.objects.get(id=pk)
    
    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = Responsible.objects.get(id=request.POST['responsible'])
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

def DeleteDetailView(request, pk):

    record = Detail.objects.get(id=pk)
    
    if request.POST:
        record.delete()

        return redirect('detail')

    return render(request=request, template_name='delete.html')