from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator


# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date                    = models.DateTimeField(auto_now_add=True)
	emergency_service_id    = models.CharField(max_length=50, blank=False)
	
	emergency_service_title = models.TextField(blank=True)
	emergency_service_txt   = models.TextField(blank=True)
	emergency_service_icon  = models.FileField(max_length=100, blank=True)
	
	status                  = models.CharField(validators=[RegexValidator], max_length=180, default='inactive') #option-> active, inactive 
	
	# Backup Fields
	trash                   = models.BooleanField(default=False)
	
	def __str__(self):
		return self.emergency_service_id