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
    path('sign/up/', views.SignUpView, name='sign-up'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='log-out'),
    path('print/excel/', views.PrintFilterToExcelView, name='print-filter-excel'),
    path('print/excel/<int:pk>/', views.print_to_excel, name='print-excel'),

    path('work/axe/', views.ListComponentView, name='work-axe'),
    path('work/axe/create/', views.CreateComponentView, name='work-axe-create'),
    path('work/axe/update/<int:pk>/', views.UpdateComponentView, name='work-axe-update'),
    path('work/axe/delete/<int:pk>/', views.DeleteComponentView, name='work-axe-delete'),

    path('responsible/', views.ListResponsibleView, name='responsible'),
    path('responsible/create/', views.CreateResponsibleView, name='responsible-create'),
    path('responsible/update/<int:pk>/', views.UpdateResponsibleView, name='responsible-update'),
    path('responsible/delete/<int:pk>/', views.DeleteResponsibleView, name='responsible-delete'),

    path('activity/', views.ListActivityView, name='activity'),
    path('activity/create/', views.CreateActivityView, name='activity-create'),
    path('activity/update/<int:pk>/', views.UpdateActivityView, name='activity-update'),
    path('activity/delete/<int:pk>/', views.DeleteActivityView, name='activity-delete'),

    path('', views.ListMasterPlanView, name='master-plan'),
    path('master/plan/create/', views.CreateMasterPlanView, name='master-plan-create'),
    path('master/plan/update/<int:pk>/', views.UpdateMasterPlanView, name='master-plan-update'),
    path('master/plan/delete/<int:pk>/', views.DeleteMasterPlanView, name='master-plan-delete'),
    path('master/plan/details/<int:pk>/', views.MasterDetailView, name='master-details'),

    path('detail/', views.ListDetailView, name='detail'),
    path('detail/create/', views.CreateDetailView, name='detail-create'), 
    path('detail/info/<int:pk>/', views.DetailInfoView, name='detail-info'),
    path('detail/create/<int:pk>/', views.CreateMasterDetailView, name='master-detail-create'), 
    path('detail/update/<int:pk>/', views.UpdateDetailView, name='detail-update'),
    path('detail/delete/<int:pk>/', views.DeleteDetailView, name='detail-delete'),
]
