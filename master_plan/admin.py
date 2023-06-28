from django.contrib import admin
from .models import CustomUser, WorkAxe, Activitie, MasterPlan, Detail

admin.site.register(CustomUser)
admin.site.register(WorkAxe)
admin.site.register(Activitie)
admin.site.register(MasterPlan)
admin.site.register(Detail)