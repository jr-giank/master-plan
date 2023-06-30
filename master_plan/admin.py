from django.contrib import admin
from .models import CustomUser, Component, Activitie, MasterPlan, Detail

admin.site.register(CustomUser)
admin.site.register(Component)
admin.site.register(Activitie)
admin.site.register(MasterPlan)
admin.site.register(Detail)