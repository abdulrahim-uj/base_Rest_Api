from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import baseapp.views
from baseapp.views import TaskViewSet, DueTaskViewSet, CompletedTaskViewSet


# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register('tasks', TaskViewSet, basename="baseapp")
router.register('completed-tasks', CompletedTaskViewSet)
router.register('pending-tasks', DueTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', baseapp.views.CreateUserTaskView.as_view(), name="user"),
    path('api-auth/', include('rest_framework.urls',)),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
/tasks/, /register/, /login/, /logout/, /completed-tasks/, /pending-tasks/
"""