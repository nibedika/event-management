from django.urls import path
from apps.backend_apps.emergency_service import views
 
urlpatterns = [
    path('add-emergency-service/', views.Emergency_service.add_emergency_service, name='add_emergency_service'),
    path('all-emergency-service/', views.Emergency_service.all_emergency_service, name='all_emergency_service'),
    path('view-emergency-service/<id>/', views.Emergency_service.view_emergency_service, name='view_emergency_service'),
    path('edit-emergency-service/<id>/', views.Emergency_service.edit_emergency_service, name='edit_emergency_service'),
    path('delete-emergency-service/<id>/', views.Emergency_service.delete_emergency_service, name='delete_emergency_service'),
]