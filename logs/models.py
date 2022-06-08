""" Models for the logs app """

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


WORK_COMPLETED = ((0, 'No'), (1, 'Yes'))
PERMISSION = ((0, 'Granted'), (1, 'Denied'), (2, 'N/A'))
SWITCH_OUT_REQUIRED = ((0, 'Yes'), (1, 'No'))
TRAFFIC_MANAGEMENT_REQUIRED = ((0, 'Yes'), (1, 'No'))


class LineVoltage(models.Model):
    """ Line Voltage """
    line_voltage = models.CharField(
        max_length=10,
        unique=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f'{self.line_voltage}'


class TreeCategory(models.Model):
    """ Tree category """
    tree_category = models.CharField(
        max_length=10,
        unique=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f'{self.tree_category}'


class ToolsRequired(models.Model):
    """ Tools Required """
    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
    )

    friendly_name = models.SlugField(
        max_length=50,
        unique=True,
        blank=False,
    )

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs):
        """
        Override the original save method to slugify the name
        """
        self.friendly_name = slugify(self.name)
        super().save(*args, **kwargs)


class PreWorkPlan(models.Model):
    """ Pre Work Plan """
    surveyor_name = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    reference_number = models.IntegerField(
        null=False,
        blank=False,
        )
    line_voltage = models.ForeignKey(
        LineVoltage,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    latitude = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )
    longitude = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )
    nearest_sub_number = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )
    landowner_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    landowner_address = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    landowner_phone_number = models.IntegerField(
        null=True,
        blank=True,
    )
    permission = models.IntegerField(
        choices=PERMISSION,
        default=0,
        )
    work_description = models.TextField(
        blank=False,
    )
    tree_category = models.ForeignKey(
        TreeCategory,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    hours_to_complete = models.IntegerField(
        blank=False,
    )
    number_of_crew_members = models.IntegerField(
        blank=False,
    )
    switch_out_required = models.IntegerField(
        choices=SWITCH_OUT_REQUIRED,
        default=1,
        blank=False
        )
    traffic_management_required = models.IntegerField(
        choices=TRAFFIC_MANAGEMENT_REQUIRED,
        default=1,
        blank=False,
        )
    tools_required_1 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='tools_required_1',
    )
    tools_required_2 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_2',
    )
    tools_required_3 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_3',
    )
    tools_required_4 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_4',
    )
    tools_required_5 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_5',
    )
    tools_required_6 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_6',
    )
    tools_required_7 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_7',
    )
    tools_required_8 = models.ForeignKey(
        ToolsRequired,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='tools_required_8',
    )
    site_safety_hazards = models.TextField(
        blank=False,
    )
    site_environmental_hazards = models.TextField(
        blank=False,
    )
    work_completed = models.IntegerField(
        choices=WORK_COMPLETED,
        default=0,
        blank=False
        )
