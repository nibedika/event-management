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
	date               = models.DateTimeField(auto_now_add=True)
	picnic_id          = models.CharField(max_length=50, blank=False)
	
	picnic_name        = models.CharField(max_length=250, blank=False)
	picnic_place       = models.CharField(max_length=250, blank=False)
	picnic_budget      = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
	picnic_description = models.TextField(blank=True)
	
	staff_id           = models.ManyToManyField(staffDB, related_name='picnic_staff_id', blank=True)
	
	status             = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash              = models.BooleanField(default=False)
	
	def __str__(self):
		return self.picnic_id