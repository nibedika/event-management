from django.urls import path
from apps.backend_apps.client import views
 
urlpatterns = [
    path('add-client/', views.Client.add_client, name='add_client'),
    path('all-client/', views.Client.all_client, name='all_client'),
    path('view-client/<id>/', views.Client.view_client, name='view_client'),
    path('edit-client/<id>/', views.Client.edit_client, name='edit_client'),
    path('delete-client/<id>/', views.Client.delete_client, name='delete_client'),
]