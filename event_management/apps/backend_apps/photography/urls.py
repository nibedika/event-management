from django.urls import path
from apps.backend_apps.photography import views
 
urlpatterns = [
    path('add-photography/', views.Photography.add_photography, name='add_photography'),
    path('all-photography/', views.Photography.all_photography, name='all_photography'),
    path('view-photography/<id>/', views.Photography.view_photography, name='view_photography'),
    path('edit-photography/<id>/', views.Photography.edit_photography, name='edit_photography'),
    path('delete-photography/<id>/', views.Photography.delete_photography, name='delete_photography'),
]