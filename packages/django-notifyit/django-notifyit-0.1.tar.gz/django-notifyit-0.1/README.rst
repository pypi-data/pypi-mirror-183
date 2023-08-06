=====
NotifyIt
=====

NotifyIt is a Django app to conduct Web-based notification. User can create a notification for other services.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django-notifyit',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('notifyit/', include('django-notifyit.urls')),

3. Run ``python manage.py migrate`` to create the notifyit models.

4. Start the development server and visit POST: http://127.0.0.1:8000/notifyit/
   to create a notification.

5. Visit GET: http://127.0.0.1:8000/notifyit/ to get list of notifications.