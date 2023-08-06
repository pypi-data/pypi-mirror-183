from django.contrib import admin
from django.urls import path
from notifications.views import NotificationListCreate, NotificationRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("", NotificationListCreate.as_view(), name="notification-list-create"),
    path("<int:pk>", NotificationRetrieveUpdateDestroyAPIView.as_view(), name="notification-retrieve-update-destroy"),
]
