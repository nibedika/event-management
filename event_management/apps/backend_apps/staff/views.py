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
from apps.backend_apps.staff.models import Cl as staffCL


# Create your views here.
class Staff():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_staff(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('staff_add'):

				# Data entry block start 
				data = staffCL(
					staff_id     = hp.unique_custom_id(hp, 'S'),
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					staff_image    = hp.file_processor(hp, request.FILES.get('staff_image'), 'staff_image', 'staff_image/'),
				)
				status = data.save()
				return redirect('all_staff')
			
			elif request.method == 'GET':
				return render(request, 'staff_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'staff_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_staff(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			staffWhere = Q_set(trash=False)
			staffInfo  = staffCL.objects.filter(staffWhere)

			return render(request, 'staff_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def view_staff(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			staffWhere = Q_set(id=id, trash=False)
			staffInfo  = staffCL.objects.get(staffWhere)

			return render(request, 'staff_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def edit_staff(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			staffWhere = Q_set(id=id, trash=False)
			staffInfo  = staffCL.objects.get(staffWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('staff_edit'):

				if request.FILES.get('staff_image') != None and request.FILES.get('staff_image') != '':
					staffImage = hp.file_processor(hp, request.FILES.get('staff_image'), 'staff_image', 'staff_image/')
				else:
					staffImage = staffInfo.staff_image

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = staffCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					staff_image    = staffImage,
					status         = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('all_staff') 

			elif request.method == 'GET':
				return render(request, 'staff_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'staffData': staffInfo})
			
			return render(request, 'staff_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'staffData': staffInfo})
		else:
			return redirect('home')



	def delete_staff(request, id):
		if request.session.has_key('username'):

			staffWhere = Q_set(id=id, trash=False)
			staffInfo  = staffCL.objects.get(staffWhere)

			staffInfo.delete()
			return redirect('all_staff')
		else:
			return redirect('home')

