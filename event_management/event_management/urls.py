"""event_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# For Media URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Access App's Urls
    path('access/', include('apps.access_apps.access.urls'), name='access'),

    # Backend App's Urls
    path('about/', include('apps.backend_apps.about.urls'), name='about'),
    path('service/', include('apps.backend_apps.service.urls'), name='service'),
    path('emergency-service/', include('apps.backend_apps.emergency_service.urls'), name='emergency_service'),
    path('photography/', include('apps.backend_apps.photography.urls'), name='photography'),
    path('sponsor/', include('apps.backend_apps.sponsor.urls'), name='sponsor'),
    path('client/', include('apps.backend_apps.client.urls'), name='client'),
    path('staff/', include('apps.backend_apps.staff.urls'), name='staff'),
    path('event/', include('apps.backend_apps.event.urls'), name='event'),
    path('package/', include('apps.backend_apps.package.urls'), name='package'),
    path('booking/', include('apps.backend_apps.booking.urls'), name='booking'),
    path('picnic/', include('apps.backend_apps.picnic.urls'), name='picnic'),
    path('feedback/', include('apps.backend_apps.feedback.urls'), name='feedback'),
    path('contact/', include('apps.backend_apps.contact.urls'), name='contact'),

    # Frontend App's Urls
    # path('website/', include('apps.frontend_apps.website.urls'), name='website'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
