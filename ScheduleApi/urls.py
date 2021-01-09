
from django.urls import path
from . import views

urlpatterns = [
    path('ping/',views.Ping, name='ping'),
  	path('', views.TaskSchedule, name="TaskSchedule"),
  	path('<str:url>/', views.Schedule, name="Schedule"),
]