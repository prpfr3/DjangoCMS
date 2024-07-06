from django.contrib import admin
from mvs.models import *


class MilitaryVehicleClassAdmin(admin.ModelAdmin):
    list_display = ["id", "mvclass", "description", "wikislug"]
    search_fields = ["mvclass", "description"]
    ordering = ("mvclass",)


admin.site.register(MilitaryVehicleClass, MilitaryVehicleClassAdmin)
