""" Admin for logs """

from django.contrib import admin
from .models import ToolsRequired, TreeCategory, LineVoltage, PreWorkPlan


class LineVoltageAdmin(admin.ModelAdmin):
    """ Line Voltage admin view """
    list_display = (
        'line_voltage',
    )

    class Meta:
        """ Change verbose name """
        verbose_name_plural = 'Line Voltages'

class TreeCategoryAdmin(admin.ModelAdmin):
    """ Tree category admin view """
    list_display = (
        'tree_category',
    )

    class Meta:
        """ Change verbose name """
        verbose_name_plural = 'Tree Categories'


class ToolsRequiredAdmin(admin.ModelAdmin):
    """ Tools Required admin view """
    list_display = (
        'name',
    )

    class Meta:
        """ Change verbose name """
        verbose_name_plural = 'Tools Required'


class PreWorkPlanAdmin(admin.ModelAdmin):
    """ Pre Work Plan admin view """
    list_display = (
        'reference_number',
        'date',
        'surveyor_name',
        'nearest_sub_number',
        'permission',
        'hours_to_complete',
        'number_of_crew_members',
        'work_completed',
    )

admin.site.register(LineVoltage, LineVoltageAdmin)
admin.site.register(ToolsRequired, ToolsRequiredAdmin)
admin.site.register(TreeCategory, TreeCategoryAdmin)
admin.site.register(PreWorkPlan, PreWorkPlanAdmin)
