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
from apps.backend_apps.sponsor.models import Cl as sponsorCL


# Create your views here.
class Sponsor():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_sponsor(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('sponsor_add'):

				# Data entry block start 
				data = sponsorCL(
					sponsor_id     = hp.unique_custom_id(hp, 'S'),
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					sponsor_image  = hp.file_processor(hp, request.FILES.get('sponsor_image'), 'sponsor_image', 'sponsor_image/'),
				)
				status = data.save()
				return redirect('all_sponsor')
			
			elif request.method == 'GET':
				return render(request, 'sponsor_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'sponsor_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_sponsor(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			sponsorWhere = Q_set(trash=False)
			sponsorInfo  = sponsorCL.objects.filter(sponsorWhere)

			return render(request, 'sponsor_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'sponsorData': sponsorInfo})
		else:
			return redirect('home')



	def view_sponsor(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			sponsorWhere = Q_set(id=id, trash=False)
			sponsorInfo  = sponsorCL.objects.get(sponsorWhere)

			return render(request, 'sponsor_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'sponsorData': sponsorInfo})
		else:
			return redirect('home')



	def edit_sponsor(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			sponsorWhere = Q_set(id=id, trash=False)
			sponsorInfo  = sponsorCL.objects.get(sponsorWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('sponsor_edit'):

				if request.FILES.get('sponsor_image') != None and request.FILES.get('sponsor_image') != '':
					sponsorImage = hp.file_processor(hp, request.FILES.get('sponsor_image'), 'sponsor_image', 'sponsor_image/')
				else:
					sponsorImage = sponsorInfo.sponsor_image

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = sponsorCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					name           = request.POST.get('name'),
					designation    = request.POST.get('designation'),
					contact        = request.POST.get('contact'),
					email          = request.POST.get('email'),
					description    = request.POST.get('description'),
					sponsor_image  = sponsorImage,
					status         = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('all_sponsor') 

			elif request.method == 'GET':
				return render(request, 'sponsor_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'sponsorData': sponsorInfo})
			
			return render(request, 'sponsor_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'sponsorData': sponsorInfo})
		else:
			return redirect('home')



	def delete_sponsor(request, id):
		if request.session.has_key('username'):

			sponsorWhere = Q_set(id=id, trash=False)
			sponsorInfo  = sponsorCL.objects.get(sponsorWhere)

			sponsorInfo.delete()
			return redirect('all_sponsor')
		else:
			return redirect('home')

