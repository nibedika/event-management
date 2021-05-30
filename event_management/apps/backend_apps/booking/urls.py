from django.urls import path
from apps.backend_apps.booking import views
 
urlpatterns = [
    path('add-booking/', views.Booking.add_booking, name='add_booking'),
    path('all-booking/', views.Booking.all_booking, name='all_booking'),
    path('view-booking/<id>/', views.Booking.view_booking, name='view_booking'),
    path('edit-booking/<id>/', views.Booking.edit_booking, name='edit_booking'),
    path('delete-booking/<id>/', views.Booking.delete_booking, name='delete_booking'),
]