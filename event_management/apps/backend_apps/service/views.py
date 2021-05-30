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
from apps.backend_apps.service.models import Cl as serviceCL


# Create your views here.
class Service():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_service(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('service_add'):

				# Data entry block start 
				data = serviceCL(
					service_id    = hp.unique_custom_id(hp, 'SEI'),
					service_title = request.POST.get('service_title'),
					service_txt   = request.POST.get('service_txt'),
					service_icon  = hp.file_processor(hp, request.FILES.get('service_icon'), 'service_icon', 'service_icon/'),
				)
				status = data.save()
				return redirect('all_service')
			
			elif request.method == 'GET':
				return render(request, 'service_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'service_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_service(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			serviceWhere = Q_set(trash=False)
			serviceInfo  = serviceCL.objects.filter(serviceWhere)

			return render(request, 'service_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'serviceData': serviceInfo})
		else:
			return redirect('home')



	def view_service(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			serviceWhere = Q_set(id=id, trash=False)
			serviceInfo  = serviceCL.objects.get(serviceWhere)

			return render(request, 'service_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'serviceData': serviceInfo})
		else:
			return redirect('home')



	def edit_service(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			serviceWhere = Q_set(id=id, trash=False)
			serviceInfo  = serviceCL.objects.get(serviceWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('service_edit'):

				if request.FILES.get('service_icon') != None and request.FILES.get('service_icon') != '':
					serviceIcon = hp.file_processor(hp, request.FILES.get('service_icon'), 'service_icon', 'service_icon/')
				else:
					serviceIcon = serviceInfo.service_icon

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = serviceCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					service_title = request.POST.get('service_title'),
					service_txt   = request.POST.get('service_txt'),
					status        = request.POST.get('status'),
					service_icon  = serviceIcon
			    )
				# Data entry block end
				return redirect('all_service') 

			elif request.method == 'GET':
				return render(request, 'service_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'serviceData': serviceInfo})
			
			return render(request, 'service_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'serviceData': serviceInfo})
		else:
			return redirect('home')



	def delete_service(request, id):
		if request.session.has_key('username'):

			serviceWhere = Q_set(id=id, trash=False)
			serviceInfo  = serviceCL.objects.get(serviceWhere)

			serviceInfo.delete()
			return redirect('all_service')
		else:
			return redirect('home')
