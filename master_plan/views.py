from django.shortcuts import render, redirect
from .forms import WorkAxeForm, ActivitieForm, ResponsibleForm, DateForm
from .models import Date, Work_axe, Activitie, Responsible

def index(request):

    activities = Date.objects.all()
            
    return render(request=request, template_name='index.html', context={'activities': activities})

def Work_axe(request):

    if request.method == 'POST':
        form = WorkAxeForm(request.POST)

        if form.is_valid():
            work_axe = Work_axe.objects.create()
            work_axe.name = request.POST['name']
            work_axe.save()

            return redirect('index')
    else:
        form = WorkAxeForm()

    return render(request=request, template_name='generic.html', context={'form': form})