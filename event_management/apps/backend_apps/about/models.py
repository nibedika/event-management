from django.db import models
from django import forms

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.core.validators import validate_image_file_extension
from django.core.validators import URLValidator

# Create your models here.
class Cl(models.Model):

	# General Info Fields
	date      = models.DateTimeField(auto_now_add=True)
	about_id  = models.CharField(max_length=50, blank=False)
	about_txt = models.TextField(blank=True)
	about_img = models.FileField(max_length=100, blank=True)
	cv_file   = models.FileField(max_length=100, blank=True)
	home_img  = models.FileField(max_length=100, blank=True)
	
	# Backup Fields
	trash     = models.BooleanField(default=False)
	
	def __str__(self):
		return self.about_id