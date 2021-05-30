from django.urls import path
from apps.backend_apps.about import views
 
urlpatterns = [
    path('add-about/', views.About.add_about, name='add_about'),
    path('all-about/', views.About.all_about, name='all_about'),
    path('view-about/<id>/', views.About.view_about, name='view_about'),
    path('edit-about/<id>/', views.About.edit_about, name='edit_about'),
    path('delete-about/<id>/', views.About.delete_about, name='delete_about'),
]