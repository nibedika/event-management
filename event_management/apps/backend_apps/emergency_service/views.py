# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.contact.models import Cl as contactCL
from apps.backend_apps.emergency_service.models import Cl as emergencyServiceCL


# Create your views here.
class Emergency_service():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_emergency_service(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('emergency_service_add'):

				# Data entry block start 
				data = emergencyServiceCL(
					emergency_service_id    = hp.unique_custom_id(hp, 'SEI'),
					emergency_service_title = request.POST.get('emergency_service_title'),
					emergency_service_txt   = request.POST.get('emergency_service_txt'),
					emergency_service_icon  = hp.file_processor(hp, request.FILES.get('emergency_service_icon'), 'emergency_service_icon', 'emergency_service_icon/'),
				)
				status = data.save()
				return redirect('all_emergency_service')
			
			elif request.method == 'GET':
				return render(request, 'emergency_service_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'emergency_service_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_emergency_service(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			emergencyServiceWhere = Q_set(trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.filter(emergencyServiceWhere)

			return render(request, 'emergency_service_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'emergencyServiceData': emergencyServiceInfo})
		else:
			return redirect('home')



	def view_emergency_service(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			emergencyServiceWhere = Q_set(id=id, trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.get(emergencyServiceWhere)

			return render(request, 'emergency_service_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'emergencyServiceData': emergencyServiceInfo})
		else:
			return redirect('home')



	def edit_emergency_service(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			emergencyServiceWhere = Q_set(id=id, trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.get(emergencyServiceWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('emergency_service_edit'):

				if request.FILES.get('emergency_service_icon') != None and request.FILES.get('emergency_service_icon') != '':
					emergencyServiceIcon = hp.file_processor(hp, request.FILES.get('emergency_service_icon'), 'emergency_service_icon', 'emergency_service_icon/')
				else:
					emergencyServiceIcon = emergencyServiceInfo.emergency_service_icon

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = emergencyServiceCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					emergency_service_title = request.POST.get('emergency_service_title'),
					emergency_service_txt   = request.POST.get('emergency_service_txt'),
					status                  = request.POST.get('status'),
					emergency_service_icon  = emergencyServiceIcon
			    )
				# Data entry block end
				return redirect('all_emergency_service') 

			elif request.method == 'GET':
				return render(request, 'emergency_service_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'emergencyServiceData': emergencyServiceInfo})
			
			return render(request, 'emergency_service_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'emergencyServiceData': emergencyServiceInfo})
		else:
			return redirect('home')



	def delete_emergency_service(request, id):
		if request.session.has_key('username'):

			emergencyServiceWhere = Q_set(id=id, trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.get(emergencyServiceWhere)

			emergencyServiceInfo.delete()
			return redirect('all_emergency_service')
		else:
			return redirect('home')
