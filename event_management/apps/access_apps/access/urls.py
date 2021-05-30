from django.urls import path
from apps.access_apps.access import views
 
urlpatterns = [
    path('sign-up/', views.Access.sign_up, name='sign_up'),
    path('sign-in/', views.Access.sign_in, name='sign_in'),
    path('sign-out/', views.Access.sign_out, name='sign_out'),

    path('website/', views.Access.web_home, name='web_home'),
    
    path('admin-panel/', views.Access.home, name='home'),
    path('view-profile/', views.Access.view_profile, name='view_profile'),
    path('edit-profile/', views.Access.edit_profile, name='edit_profile'),
]