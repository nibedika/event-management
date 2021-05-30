from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

from apps.backend_apps.event.models import Cl as eventDB


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date                = models.DateTimeField(auto_now_add=True)
	booking_id          = models.CharField(max_length=50, blank=False)
	
	booking_for         = models.CharField(max_length=250, blank=False)
	booking_description = models.TextField(blank=True)
	booking_remark      = models.TextField(blank=True)
	
	event_id            = models.ForeignKey(eventDB, on_delete=models.CASCADE, related_name='booking_event_id')
	
	status              = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash               = models.BooleanField(default=False)
	
	def __str__(self):
		return self.booking_id