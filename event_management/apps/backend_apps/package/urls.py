from django.urls import path
from apps.backend_apps.package import views
 
urlpatterns = [
    path('add-package/', views.Package.add_package, name='add_package'),
    path('all-package/', views.Package.all_package, name='all_package'),
    path('view-package/<id>/', views.Package.view_package, name='view_package'),
    path('edit-package/<id>/', views.Package.edit_package, name='edit_package'),
    path('delete-package/<id>/', views.Package.delete_package, name='delete_package'),
]