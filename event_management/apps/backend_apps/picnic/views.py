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
from apps.backend_apps.picnic.models import Cl as picnicCL
from apps.backend_apps.staff.models import Cl as staffCL


# Create your views here.
class Picnic():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_picnic(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# STAFF
			staffWhere = Q_set(status='active', trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('picnic_add'):

				picnicId = hp.unique_custom_id(hp, 'E')

				# Data entry block start 
				data = picnicCL(
					picnic_id          = picnicId,
					picnic_name        = request.POST.get('picnic_name'),
					picnic_place       = request.POST.get('picnic_place'),
					picnic_budget      = request.POST.get('picnic_budget'),
					picnic_description = request.POST.get('picnic_description'),
				)
				status    = data.save()
				where     = Q_set(picnic_id=picnicId, trash=False)
				addedInfo = picnicCL.objects.get(where)

				for staff in request.POST.getlist('staff_id[]'):
					stWhere = Q_set(staff_id=staff, status='active', trash=False)
					stInfo  = staffCL.objects.get(stWhere)
					addedInfo.staff_id.add(stInfo)

				return redirect('all_picnic')
			
			elif request.method == 'GET':
				return render(request, 'picnic_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'staffData': staffInfo})

			return render(request, 'picnic_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def all_picnic(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			picnicWhere = Q_set(trash=False)
			picnicInfo  = picnicCL.objects.filter(picnicWhere)

			return render(request, 'picnic_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'picnicData': picnicInfo})
		else:
			return redirect('home')



	def view_picnic(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			picnicWhere = Q_set(id=id, trash=False)
			picnicInfo  = picnicCL.objects.get(picnicWhere)

			# STAFF
			staffWhere = Q_set(status='active', trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			return render(request, 'picnic_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'picnicData': picnicInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def edit_picnic(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			picnicWhere = Q_set(id=id, trash=False)
			picnicInfo  = picnicCL.objects.get(picnicWhere)

			# STAFF
			staffWhere = Q_set(status='active', trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('picnic_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = picnicCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					picnic_name        = request.POST.get('picnic_name'),
					picnic_place       = request.POST.get('picnic_place'),
					picnic_budget      = request.POST.get('picnic_budget'),
					picnic_description = request.POST.get('picnic_description'),
			    )
				# Data entry block end
				where     = Q_set(picnic_id=picnicInfo.picnic_id, trash=False)
				addedInfo = picnicCL.objects.get(where)

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

				return redirect('all_picnic') 

			elif request.method == 'GET':
				return render(request, 'picnic_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'picnicData': picnicInfo, 'staffData': staffInfo})
			
			return render(request, 'picnic_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'picnicData': picnicInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def delete_picnic(request, id):
		if request.session.has_key('username'):

			picnicWhere = Q_set(id=id, trash=False)
			picnicInfo  = picnicCL.objects.get(picnicWhere)

			picnicInfo.delete()
			return redirect('all_picnic')
		else:
			return redirect('home')
