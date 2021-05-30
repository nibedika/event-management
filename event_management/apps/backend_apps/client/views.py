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
from apps.backend_apps.client.models import Cl as clientCL


# Create your views here.
class Client():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_client(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('client_add'):

				# Data entry block start 
				data = clientCL(
					client_id     = hp.unique_custom_id(hp, 'S'),
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					client_image   = hp.file_processor(hp, request.FILES.get('client_image'), 'client_image', 'client_image/'),
				)
				status = data.save()
				return redirect('all_client')
			
			elif request.method == 'GET':
				return render(request, 'client_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'client_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_client(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			clientWhere = Q_set(trash=False)
			clientInfo  = clientCL.objects.filter(clientWhere)

			return render(request, 'client_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'clientData': clientInfo})
		else:
			return redirect('home')



	def view_client(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			clientWhere = Q_set(id=id, trash=False)
			clientInfo  = clientCL.objects.get(clientWhere)

			return render(request, 'client_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'clientData': clientInfo})
		else:
			return redirect('home')



	def edit_client(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			clientWhere = Q_set(id=id, trash=False)
			clientInfo  = clientCL.objects.get(clientWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('client_edit'):

				if request.FILES.get('client_image') != None and request.FILES.get('client_image') != '':
					clientImage = hp.file_processor(hp, request.FILES.get('client_image'), 'client_image', 'client_image/')
				else:
					clientImage = clientInfo.client_image

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = clientCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					client_image   = clientImage,
					status         = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('all_client') 

			elif request.method == 'GET':
				return render(request, 'client_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'clientData': clientInfo})
			
			return render(request, 'client_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'clientData': clientInfo})
		else:
			return redirect('home')



	def delete_client(request, id):
		if request.session.has_key('username'):

			clientWhere = Q_set(id=id, trash=False)
			clientInfo  = clientCL.objects.get(clientWhere)

			clientInfo.delete()
			return redirect('all_client')
		else:
			return redirect('home')

