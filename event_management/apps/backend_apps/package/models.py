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
	package_id           = models.CharField(max_length=50, blank=False)
	
	package_name         = models.CharField(max_length=250, blank=False)
	package_value        = models.CharField(max_length=250, blank=False)
	people_preference    = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
	package_description  = models.TextField(blank=True)
	package_remark       = models.TextField(blank=True)
	package_file         = models.FileField(max_length=100, blank=True)
	
	service_id           = models.ManyToManyField(serviceDB, related_name='package_service_id', blank=True)
	emergency_service_id = models.ManyToManyField(emergencyServiceDB, related_name='package_emergency_service_id', blank=True)
	sponsor_id           = models.ManyToManyField(sponsorDB, related_name='package_sponsor_id', blank=True)
	client_id            = models.ForeignKey(clientDB, on_delete=models.CASCADE, related_name='package_client_id')
	staff_id             = models.ManyToManyField(staffDB, related_name='package_staff_id', blank=True)
	
	regular_price        = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
	current_price        = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
	
	status               = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash                = models.BooleanField(default=False)
	
	def __str__(self):
		return self.package_id