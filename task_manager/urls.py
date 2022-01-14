from django.contrib import admin
from django.urls import path

from tasks.views import add_task, complete_task, completed_task_view, delete_task, home_view, task_view


urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path('', home_view),
    path('tasks', task_view),
    path('pending_tasks', task_view),
    path('all_tasks', home_view),
    path('completed_tasks', completed_task_view),
    path('add-task', add_task),
    path('complete_task/<int:index>', complete_task),
    path('delete-task/<int:index>', delete_task),
]
