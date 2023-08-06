import time

import pika
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from notifications.connection import Connection
from notifications.producer import Publisher
from notifications.serializers import NotificationSerializer
from notifications.models import Notification


class NotificationListCreate(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = None
    permission_classes = []


class NotificationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = None
    permission_classes = []
