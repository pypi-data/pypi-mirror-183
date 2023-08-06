from django.utils.translation import gettext_lazy as _
from django.db.models import IntegerChoices


class ServiceType(IntegerChoices):
    """Notification Service Type"""
    SERVICE1 = 1, _('SERVICE1')
    SERVICE2 = 2, _('SERVICE2')
    SERVICE3 = 3, _('SERVICE3')
    SERVICE4 = 4, _('SERVICE4')
