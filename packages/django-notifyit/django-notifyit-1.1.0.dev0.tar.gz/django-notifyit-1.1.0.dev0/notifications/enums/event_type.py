from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerChoices


class EventType(IntegerChoices):
    """Notification Event Type"""
    CREATE = 1, _('Create New Notification')
    UPDATE = 2, _('Update Existing Notification')
