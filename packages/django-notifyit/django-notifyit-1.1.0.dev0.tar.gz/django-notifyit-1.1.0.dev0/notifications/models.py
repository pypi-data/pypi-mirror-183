from django.db import models

from notifications.enums import EventType, ServiceType


class Notification(models.Model):
    """Generic/Abstract Poll with common fields used for Inheritance"""
    icon = models.PositiveSmallIntegerField(verbose_name='Icon')
    sub_icon = models.PositiveSmallIntegerField(verbose_name='Sub icon')
    event_creator = models.PositiveSmallIntegerField(choices=ServiceType.choices, 
                                                    default=ServiceType.SERVICE1, verbose_name='Creator')
    title = models.CharField(max_length=28, verbose_name='Title')
    context = models.TextField(max_length=95, verbose_name='Description')
    event_type = models.PositiveSmallIntegerField(choices=EventType.choices, default=EventType.CREATE, verbose_name='Type')
    dynamic_link = models.CharField(max_length=256, verbose_name='Dynamic link')
    viewed = models.BooleanField(default=False, verbose_name='Viewed')
    valid = models.BooleanField(default=True, verbose_name='Valid')
    valid_until = models.DateTimeField(null=True, verbose_name='Valid until timestamp')
    clicked = models.BooleanField(default=False, verbose_name='Clicked')
    clicked_at = models.DateTimeField(null=True, verbose_name='Clicked at timestamp')
    location = models.CharField(null=True, default=None, max_length=32, verbose_name='Location')
    channel = models.CharField(null=True, default=None, max_length=32, verbose_name='Channel')
    status = models.CharField(default='Not Published', max_length=16, verbose_name='Status')
    routing_key = models.CharField(max_length=32, verbose_name='Routing Key')

    def __str__(self):
        return f"{self.pk} | {self.event_creator} | {self.title}"
