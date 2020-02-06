from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todolist, name="todolist"),
    path('task/create/', views.create_task, name="create_task"),
    path('task/<int:id>/', views.detail_task, name="detail_task"),
    path('task/update/<int:id>/', views.update_task, name="update_task"),
    path('task/delete/<int:id>/', views.delete_task, name="delete_task"),
]
