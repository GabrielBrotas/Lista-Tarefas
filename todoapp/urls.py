from django.urls import path
from todoapp import views

urlpatterns = [
    path('todo/', views.index),
    path('todo/addTodo/', views.AddTodo),
    path('todo/deleteTodo/<int:todo_id>/', views.deleteTodo),
]