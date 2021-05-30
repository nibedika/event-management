from django.urls import path
from apps.backend_apps.service import views
 
urlpatterns = [
    path('add-service/', views.Service.add_service, name='add_service'),
    path('all-service/', views.Service.all_service, name='all_service'),
    path('view-service/<id>/', views.Service.view_service, name='view_service'),
    path('edit-service/<id>/', views.Service.edit_service, name='edit_service'),
    path('delete-service/<id>/', views.Service.delete_service, name='delete_service'),
]