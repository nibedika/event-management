from django.urls import path
from apps.backend_apps.staff import views
 
urlpatterns = [
    path('add-staff/', views.Staff.add_staff, name='add_staff'),
    path('all-staff/', views.Staff.all_staff, name='all_staff'),
    path('view-staff/<id>/', views.Staff.view_staff, name='view_staff'),
    path('edit-staff/<id>/', views.Staff.edit_staff, name='edit_staff'),
    path('delete-staff/<id>/', views.Staff.delete_staff, name='delete_staff'),
]