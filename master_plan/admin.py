from django.contrib import admin
from .models import CustomUser, WorkAxe, Activitie, Responsible, MasterPlan, Detail

admin.site.register(CustomUser)
admin.site.register(WorkAxe)
admin.site.register(Activitie)
admin.site.register(Responsible)
admin.site.register(MasterPlan)
admin.site.register(Detail)