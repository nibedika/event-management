# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.contact.models import set_Cl as setContactCL
from apps.backend_apps.contact.models import Cl as contactCL


# Create your views here.
class Contact():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def set_contact(request):

		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			setContactWhere = Q_set(trash=False)
			setContactInfo  = setContactCL.objects.filter(setContactWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('contact_set'):

				# Data entry block start 
				data = setContactCL(
					set_contact_id = hp.unique_custom_id(hp, 'SCI'),
					email          = request.POST.get('email'),
					contact        = request.POST.get('contact'),
					address        = request.POST.get('address'),
					facebook_url   = request.POST.get('facebook_url'),
					instagram_url  = request.POST.get('instagram_url'),
					linkedin_url   = request.POST.get('linkedin_url'),
					github_url     = request.POST.get('github_url'),
					twitter_url    = request.POST.get('twitter_url'),
					pinterest_url  = request.POST.get('pinterest_url'),
					youtube_url    = request.POST.get('youtube_url'),
				)
				status = data.save()
				return redirect('set_contact')
			
			elif request.method == 'GET':
				return render(request, 'contact_set.html', {'menuData': menuInfo, 'msgData': msgInfo, 'setContactData': setContactInfo})

			return render(request, 'contact_set.html', {'menuData': menuInfo, 'msgData': msgInfo, 'setContactData': setContactInfo})
		else:
			return redirect('home')



	def edit_set_contact(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			setContactWhere = Q_set(id=id, trash=False)
			setContactInfo  = setContactCL.objects.get(setContactWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('set_contact_edit'):

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = setContactCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					email         = request.POST.get('email'),
					contact       = request.POST.get('contact'),
					address       = request.POST.get('address'),
					facebook_url  = request.POST.get('facebook_url'),
					instagram_url = request.POST.get('instagram_url'),
					linkedin_url  = request.POST.get('linkedin_url'),
					github_url    = request.POST.get('github_url'),
					twitter_url   = request.POST.get('twitter_url'),
					pinterest_url = request.POST.get('pinterest_url'),
					youtube_url   = request.POST.get('youtube_url'),
					status        = request.POST.get('status'),
			    )
				# Data entry block end
				return redirect('set_contact') 

			elif request.method == 'GET':
				return render(request, 'contact_set_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'setContactData': setContactInfo})
			
			return render(request, 'contact_set_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'setContactData': setContactInfo})
		else:
			return redirect('home')



	def delete_set_contact(request, id):
		if request.session.has_key('username'):

			setContactWhere = Q_set(id=id, trash=False)
			setContactInfo  = setContactCL.objects.get(setContactWhere)

			setContactInfo.delete()
			return redirect('set_contact')
		else:
			return redirect('home')




###############################################################################




	def add_contact(request):

		# Add Start Here ------------->
		if request.method == 'POST' and request.POST.get('contact_add'):

			# Data entry block start 
			data = contactCL(
				contact_id  = hp.unique_custom_id(hp, 'FCI'),
				name        = request.POST.get('name'),
				contact     = request.POST.get('contact'),
				email       = request.POST.get('email'),
				subject     = request.POST.get('subject'),
				description = request.POST.get('description')
			)
			status = data.save()
			return redirect('website')
		
		elif request.method == 'GET':
			return redirect('website')



	def all_contact(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			contactWhere = Q_set(trash=False)
			contactInfo  = contactCL.objects.filter(contactWhere)

			return render(request, 'contact_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contactData': contactInfo})
		else:
			return redirect('home')



	def view_contact(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			contactWhere = Q_set(id=id, trash=False)
			contactInfo  = contactCL.objects.get(contactWhere)

			return render(request, 'contact_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'contactData': contactInfo})
		else:
			return redirect('home')



	def edit_contact(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			contactWhere = Q_set(id=id, trash=False)
			contactInfo  = contactCL.objects.get(contactWhere)

			# Data entry block start 
			where       = Q_set(id=id, trash=False)
			pre_update  = contactCL.objects.select_related().filter(where)
			post_update = pre_update.update(
				status  = 'seen',
		    )
			# Data entry block end

			return redirect('view_contact', id=id)
		else:
			return redirect('home')



	def delete_contact(request, id):
		if request.session.has_key('username'):

			contactWhere = Q_set(id=id, trash=False)
			contactInfo  = contactCL.objects.get(contactWhere)

			contactInfo.delete()
			return redirect('all_contact')
		else:
			return redirect('home')
