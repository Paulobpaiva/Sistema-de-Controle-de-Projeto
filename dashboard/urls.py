from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('activities-report/', views.activities_report, name='activities_report'),
    path('time-report/', views.time_report, name='time_report'),
] 