from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name= "task_list"),
    path("task/<int:pk>/update", views.task_update, name = "update_task"),
    path("task/<int:pk>/delete", views.task_delete, name = "delete_task"),
]