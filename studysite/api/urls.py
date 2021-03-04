from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('todolist/', views.ApiTodoLV.as_view(), name='list'),
    path('todo/<int:pk>/delete/', views.ApiTodoDelV.as_view(), name='delete'),
    path('todo/create/', views.APITodoCV.as_view(), name='create'),
]