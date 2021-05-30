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
from apps.backend_apps.event.models import Cl as eventCL
from apps.backend_apps.service.models import Cl as serviceCL
from apps.backend_apps.emergency_service.models import Cl as emergencyServiceCL
from apps.backend_apps.sponsor.models import Cl as sponsorCL
from apps.backend_apps.client.models import Cl as clientCL
from apps.backend_apps.staff.models import Cl as staffCL


# Create your views here.
class Event():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_event(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# SERVICE
			serviceWhere = Q_set(status='active', trash=False)
			serviceInfo  = serviceCL.objects.filter(serviceWhere)

			# EMERGY SERVICE
			emergencyServiceWhere = Q_set(status='active', trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.filter(emergencyServiceWhere)

			# SPONSOR
			sponsorWhere = Q_set(status='active', trash=False)
			sponsorInfo  = sponsorCL.objects.filter(sponsorWhere)

			# CLIENT
			clientWhere = Q_set(status='active', trash=False)
			clientInfo  = clientCL.objects.filter(clientWhere)

			# STAFF
			staffWhere = Q_set(status='active', trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('event_add'):

				# CLIENT
				sinclientWhere = Q_set(client_id=request.POST.get('client_id'), status='active', trash=False)
				sinclientInfo  = clientCL.objects.get(sinclientWhere)

				eventId = hp.unique_custom_id(hp, 'E')

				# Data entry block start 
				data = eventCL(
					event_id             = eventId,
					event_name           = request.POST.get('event_name'),
					event_description    = request.POST.get('event_description'),
					event_remark         = request.POST.get('event_remark'),
					client_id            = sinclientInfo,
					event_file           = hp.file_processor(hp, request.FILES.get('event_file'), 'event_file', 'event_file/'),
				)
				status    = data.save()
				where     = Q_set(event_id=eventId, trash=False)
				addedInfo = eventCL.objects.get(where)

				for service in request.POST.getlist('service_id[]'):
					sWhere = Q_set(service_id=service, status='active', trash=False)
					sInfo  = serviceCL.objects.get(sWhere)
					addedInfo.service_id.add(sInfo)


				for emergency in request.POST.getlist('emergency_service_id[]'):
					eWhere = Q_set(emergency_service_id=emergency, status='active', trash=False)
					eInfo  = emergencyServiceCL.objects.get(eWhere)
					addedInfo.emergency_service_id.add(eInfo)


				for sponsor in request.POST.getlist('sponsor_id[]'):
					spWhere = Q_set(sponsor_id=sponsor, status='active', trash=False)
					spInfo  = sponsorCL.objects.get(spWhere)
					addedInfo.sponsor_id.add(spInfo)


				for staff in request.POST.getlist('staff_id[]'):
					stWhere = Q_set(staff_id=staff, status='active', trash=False)
					stInfo  = staffCL.objects.get(stWhere)
					addedInfo.staff_id.add(stInfo)

				return redirect('all_event')
			
			elif request.method == 'GET':
				return render(request, 'event_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'serviceData': serviceInfo, 'emergencyServiceData': emergencyServiceInfo, 'sponsorData': sponsorInfo, 'clientData': clientInfo, 'staffData': staffInfo})

			return render(request, 'event_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'serviceData': serviceInfo, 'emergencyServiceData': emergencyServiceInfo, 'sponsorData': sponsorInfo, 'clientData': clientInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def all_event(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			eventWhere = Q_set(trash=False)
			eventInfo  = eventCL.objects.filter(eventWhere)

			return render(request, 'event_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'eventData': eventInfo})
		else:
			return redirect('home')



	def view_event(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			eventWhere = Q_set(id=id, trash=False)
			eventInfo  = eventCL.objects.get(eventWhere)

			# SERVICE
			serviceWhere = Q_set(status='active', trash=False)
			serviceInfo  = serviceCL.objects.filter(serviceWhere)

			# EMERGY SERVICE
			emergencyServiceWhere = Q_set(status='active', trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.filter(emergencyServiceWhere)

			# SPONSOR
			sponsorWhere = Q_set(status='active', trash=False)
			sponsorInfo  = sponsorCL.objects.filter(sponsorWhere)

			# STAFF
			staffWhere = Q_set(status='active', trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			return render(request, 'event_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'eventData': eventInfo, 'serviceData': serviceInfo, 'emergencyServiceData': emergencyServiceInfo, 'sponsorData': sponsorInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def edit_event(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			eventWhere = Q_set(id=id, trash=False)
			eventInfo  = eventCL.objects.get(eventWhere)

			# SERVICE
			serviceWhere = Q_set(status='active', trash=False)
			serviceInfo  = serviceCL.objects.filter(serviceWhere)

			# EMERGY SERVICE
			emergencyServiceWhere = Q_set(status='active', trash=False)
			emergencyServiceInfo  = emergencyServiceCL.objects.filter(emergencyServiceWhere)

			# SPONSOR
			sponsorWhere = Q_set(status='active', trash=False)
			sponsorInfo  = sponsorCL.objects.filter(sponsorWhere)

			# CLIENT
			clientWhere = Q_set(status='active', trash=False)
			clientInfo  = clientCL.objects.filter(clientWhere)

			# STAFF
			staffWhere = Q_set(status='active', trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('event_edit'):

				# CLIENT
				sinclientWhere = Q_set(client_id=request.POST.get('client_id'), status='active', trash=False)
				sinclientInfo  = clientCL.objects.get(sinclientWhere)

				if request.FILES.get('event_file') != None and request.FILES.get('event_file') != '':
					eventFile = hp.file_processor(hp, request.FILES.get('event_file'), 'event_file', 'event_file/')
				else:
					eventFile = eventInfo.event_file

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = eventCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					event_name           = request.POST.get('event_name'),
					event_description    = request.POST.get('event_description'),
					event_remark         = request.POST.get('event_remark'),
					status               = request.POST.get('status'),
					client_id            = sinclientInfo,
					event_file           = eventFile
			    )
				# Data entry block end
				where     = Q_set(event_id=eventInfo.event_id, trash=False)
				addedInfo = eventCL.objects.get(where)

				for service in request.POST.getlist('service_id[]'):
					cond = Q_set(service_id=service)
					if service in addedInfo.service_id.all():
						sWhere = Q_set(service_id=service, status='active', trash=False)
						sInfo  = serviceCL.objects.get(sWhere)
						addedInfo.service_id.remove(sInfo)
					else:
						sWhere = Q_set(service_id=service, status='active', trash=False)
						sInfo  = serviceCL.objects.get(sWhere)
						addedInfo.service_id.add(sInfo)

				for emergency_service in request.POST.getlist('emergency_service_id[]'):
					cond = Q_set(emergency_service_id=emergency_service)
					if emergency_service in addedInfo.emergency_service_id.all():
						sWhere = Q_set(emergency_service_id=emergency_service, status='active', trash=False)
						sInfo  = emergencyServiceCL.objects.get(sWhere)
						addedInfo.emergency_service_id.remove(sInfo)
					else:
						sWhere = Q_set(emergency_service_id=emergency_service, status='active', trash=False)
						sInfo  = emergencyServiceCL.objects.get(sWhere)
						addedInfo.emergency_service_id.add(sInfo)

				for sponsor in request.POST.getlist('sponsor_id[]'):
					cond = Q_set(sponsor_id=sponsor)
					if sponsor in addedInfo.sponsor_id.all():
						sWhere = Q_set(sponsor_id=sponsor, status='active', trash=False)
						sInfo  = sponsorCL.objects.get(sWhere)
						addedInfo.sponsor_id.remove(sInfo)
					else:
						sWhere = Q_set(sponsor_id=sponsor, status='active', trash=False)
						sInfo  = sponsorCL.objects.get(sWhere)
						addedInfo.sponsor_id.add(sInfo)

				for staff in request.POST.getlist('staff_id[]'):
					cond = Q_set(staff_id=staff)
					if staff in addedInfo.staff_id.all():
						sWhere = Q_set(staff_id=staff, status='active', trash=False)
						sInfo  = staffCL.objects.get(sWhere)
						addedInfo.staff_id.remove(sInfo)
					else:
						sWhere = Q_set(staff_id=staff, status='active', trash=False)
						sInfo  = staffCL.objects.get(sWhere)
						addedInfo.staff_id.add(sInfo)

				return redirect('all_event') 

			elif request.method == 'GET':
				return render(request, 'event_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'eventData': eventInfo, 'serviceData': serviceInfo, 'emergencyServiceData': emergencyServiceInfo, 'sponsorData': sponsorInfo, 'clientData': clientInfo, 'staffData': staffInfo})
			
			return render(request, 'event_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'eventData': eventInfo, 'serviceData': serviceInfo, 'emergencyServiceData': emergencyServiceInfo, 'sponsorData': sponsorInfo, 'clientData': clientInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def delete_event(request, id):
		if request.session.has_key('username'):

			eventWhere = Q_set(id=id, trash=False)
			eventInfo  = eventCL.objects.get(eventWhere)

			eventInfo.delete()
			return redirect('all_event')
		else:
			return redirect('home')
