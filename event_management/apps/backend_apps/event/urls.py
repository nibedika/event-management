from django.urls import path
from apps.backend_apps.event import views
 
urlpatterns = [
    path('add-event/', views.Event.add_event, name='add_event'),
    path('all-event/', views.Event.all_event, name='all_event'),
    path('view-event/<id>/', views.Event.view_event, name='view_event'),
    path('edit-event/<id>/', views.Event.edit_event, name='edit_event'),
    path('delete-event/<id>/', views.Event.delete_event, name='delete_event'),
]