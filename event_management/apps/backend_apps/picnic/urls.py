from django.urls import path
from apps.backend_apps.picnic import views
 
urlpatterns = [
    path('add-picnic/', views.Picnic.add_picnic, name='add_picnic'),
    path('all-picnic/', views.Picnic.all_picnic, name='all_picnic'),
    path('view-picnic/<id>/', views.Picnic.view_picnic, name='view_picnic'),
    path('edit-picnic/<id>/', views.Picnic.edit_picnic, name='edit_picnic'),
    path('delete-picnic/<id>/', views.Picnic.delete_picnic, name='delete_picnic'),
]