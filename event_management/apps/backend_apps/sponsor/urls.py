from django.urls import path
from apps.backend_apps.sponsor import views
 
urlpatterns = [
    path('add-sponsor/', views.Sponsor.add_sponsor, name='add_sponsor'),
    path('all-sponsor/', views.Sponsor.all_sponsor, name='all_sponsor'),
    path('view-sponsor/<id>/', views.Sponsor.view_sponsor, name='view_sponsor'),
    path('edit-sponsor/<id>/', views.Sponsor.edit_sponsor, name='edit_sponsor'),
    path('delete-sponsor/<id>/', views.Sponsor.delete_sponsor, name='delete_sponsor'),
]