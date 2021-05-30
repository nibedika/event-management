from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.backend_apps.service.models import Cl as serviceDB
from apps.backend_apps.emergency_service.models import Cl as emergencyServiceDB
from apps.backend_apps.sponsor.models import Cl as sponsorDB
from apps.backend_apps.client.models import Cl as clientDB
from apps.backend_apps.staff.models import Cl as staffDB


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date                 = models.DateTimeField(auto_now_add=True)
	event_id             = models.CharField(max_length=50, blank=False)
	
	event_name           = models.CharField(max_length=250, blank=False)
	event_description    = models.TextField(blank=True)
	event_remark         = models.TextField(blank=True)
	event_file           = models.FileField(max_length=100, blank=True)
	
	#service_id           = models.ForeignKey(serviceDB, on_delete=models.CASCADE, related_name='event_service_id')
	#emergency_service_id = models.ForeignKey(emergencyServiceDB, on_delete=models.CASCADE, related_name='event_emergency_service_id')
	#sponsor_id           = models.ForeignKey(sponsorDB, on_delete=models.CASCADE, related_name='event_sponsor_id')
	#client_id            = models.ForeignKey(clientDB, on_delete=models.CASCADE, related_name='event_client_id')
	#staff_id             = models.ForeignKey(staffDB, on_delete=models.CASCADE, related_name='event_staff_id')
		
	service_id           = models.ManyToManyField(serviceDB, related_name='event_service_id', blank=True)
	emergency_service_id = models.ManyToManyField(emergencyServiceDB, related_name='event_emergency_service_id', blank=True)
	sponsor_id           = models.ManyToManyField(sponsorDB, related_name='event_sponsor_id', blank=True)
	client_id            = models.ForeignKey(clientDB, on_delete=models.CASCADE, related_name='event_client_id')
	staff_id             = models.ManyToManyField(staffDB, related_name='event_staff_id', blank=True)
	
	status               = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash                = models.BooleanField(default=False)
	
	def __str__(self):
		return self.event_id