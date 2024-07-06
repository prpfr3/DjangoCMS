from django.db import models
from cms.models import CMSPlugin
from mvs.models import MilitaryVehicleClass


class MilitaryVehicleClassPluginModel(CMSPlugin):
    mv = models.ForeignKey(MilitaryVehicleClass, on_delete=models.CASCADE)

    def __str__(self):
        return self.mv.mvclass
