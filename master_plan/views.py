from django.shortcuts import render, redirect
from .forms import WorkAxeForm, ActivitieForm, ResponsibleForm, DateForm, MasterPlanForm, DetailForm
from .models import Date, WorkAxe, Activitie, Responsible, MasterPlan, Detail

def index(request):

    activities = Date.objects.all().order_by('date')
            
    return render(request=request, template_name='index.html', context={'activities': activities})

def CreateWorkAxeView(request):

    if request.method == 'POST':
        form = WorkAxeForm(request.POST)

        if form.is_valid():
            work_axe = WorkAxe.objects.create()
            work_axe.name = request.POST['name']
            work_axe.save()

            return redirect('home')
    else:
        form = WorkAxeForm()

    return render(request=request, template_name='create.html', context={'form': form})

def CreateResponsibleView(request):

    if request.method == 'POST':
        form = ResponsibleForm(request.POST)

        if form.is_valid():
            responsible = Responsible.objects.create()
            responsible.name = request.POST['name']
            responsible.save()

            return redirect('home')
    else:
        form = ResponsibleForm()

    return render(request=request, template_name='create.html', context={'form': form})

def CreateActivityView(request):

    if request.method == 'POST':
        form = ActivitieForm(request.POST)

        if form.is_valid():
            work_axe = WorkAxe.objects.get(id=request.POST['work_axe'])
            activity = Activitie.objects.create(work_axe=work_axe, name=request.POST['name'])
            
            return redirect('home')
    else:
        form = ActivitieForm()

    return render(request=request, template_name='create.html', context={'form': form})

def CreateMasterPlanView(request):

    if request.method == 'POST':
        form = MasterPlanForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.create()
            master_plan.name = request.POST['name']
            master_plan.description = request.POST['description']
            master_plan.notes = request.POST['notes']
            master_plan.save()

            return redirect('home')
    else:
        form = MasterPlanForm()

    return render(request=request, template_name='create.html', context={'form': form})

def CreateDetailView(request):

    if request.method == 'POST':
        form = DetailForm(request.POST)

        if form.is_valid():
            master_plan = MasterPlan.objects.get(id=request.POST['master_plan'])
            activity = Activitie.objects.get(id=request.POST['activity'])
            work_axe = WorkAxe.objects.get(id=activity.work_axe.id)
            responsible = Responsible.objects.get(id=request.POST['responsible'])
            
            detail = Detail.objects.create(
                master_plan=master_plan,
                work_axe=work_axe,
                activity=activity,
                responsible=responsible,
                scheduled_date=request.POST['scheduled_date'],
                completed_date=request.POST['completed_date'],
                evaluation = request.POST['evaluation'],
                observations = request.POST['observations']
            )

            return redirect('home')
    else:
        form = DetailForm()

    return render(request=request, template_name='create.html', context={'form': form})
