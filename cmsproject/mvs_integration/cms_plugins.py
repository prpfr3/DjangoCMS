from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from mvs_integration.models import MilitaryVehicleClassPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class PollPluginPublisher(CMSPluginBase):
    model = MilitaryVehicleClassPluginModel  # model where plugin data are saved
    module = _("MVS")
    name = _("MVS Class Plugin")  # name of the plugin in the interface
    render_template = "mvs_integration/mvs_class_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context
