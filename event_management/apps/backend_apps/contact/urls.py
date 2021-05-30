from django.urls import path
from apps.backend_apps.contact import views
 
urlpatterns = [
    path('set-contact/', views.Contact.set_contact, name='set_contact'),
    path('edit-set-contact/<id>/', views.Contact.edit_set_contact, name='edit_set_contact'),
    path('delete-set-contact/<id>/', views.Contact.delete_set_contact, name='delete_set_contact'),
    
    path('add-contact/', views.Contact.add_contact, name='add_contact'),
    path('all-contact/', views.Contact.all_contact, name='all_contact'),
    path('view-contact/<id>/', views.Contact.view_contact, name='view_contact'),
    path('edit-contact/<id>/', views.Contact.edit_contact, name='edit_contact'),
    path('delete-contact/<id>/', views.Contact.delete_contact, name='delete_contact'),
]