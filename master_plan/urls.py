"""
URL configuration for master_plan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView, name='home'),

    path('work/axe/', views.ListWorkAxeView, name='work-axe'),
    path('work/axe/create/', views.CreateWorkAxeView, name='work-axe-create'),
    path('work/axe/update/<int:pk>/', views.UpdateWorkAxeView, name='work-axe-update'),

    path('responsible/', views.ListResponsibleView, name='responsible'),
    path('responsible/create/', views.CreateResponsibleView, name='responsible-create'),
    path('responsible/update/<int:pk>/', views.UpdateResponsibleView, name='responsible-update'),

    path('activity/', views.ListActivityView, name='activity'),
    path('activity/create/', views.CreateActivityView, name='activity-create'),
    path('activity/update/<int:pk>/', views.UpdateActivityView, name='activity-update'),

    path('master/plan/', views.ListMasterPlanView, name='master-plan'),
    path('master/plan/create/', views.CreateMasterPlanView, name='master-plan-create'),
    path('master/plan/update/<int:pk>/', views.UpdateMasterPlanView, name='master-plan-update'),

    path('detail/', views.ListDetailView, name='detail'),
    path('detail/create/', views.CreateDetailView, name='detail-create'), 
    path('detail/update/<int:pk>/', views.UpdateDetailView, name='detail-update'),
]
