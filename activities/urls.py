from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.activity_list, name='activity_list'),
    path('create/', views.activity_create, name='activity_create'),
    path('<int:pk>/', views.activity_detail, name='activity_detail'),
    path('<int:pk>/edit/', views.activity_update, name='activity_update'),
    path('<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    path('<int:pk>/update-status/', views.update_activity_status, name='update_activity_status'),
    
    # Ações
    path('actions/', views.action_list, name='action_list'),
    path('actions/<int:pk>/', views.action_detail, name='action_detail'),
] 