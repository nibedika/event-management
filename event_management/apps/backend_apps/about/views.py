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
from apps.backend_apps.about.models import Cl as aboutCL


# Create your views here.
class About():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_about(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('about_add'):

				# Data entry block start 
				data = aboutCL(
					about_id  = hp.unique_custom_id(hp, 'ABI'),
					about_txt = request.POST.get('about_txt'),
					about_img = hp.file_processor(hp, request.FILES.get('about_img'), 'about_img', 'about_img/'),
					cv_file   = hp.file_processor(hp, request.FILES.get('cv_file'), 'cv_file', 'cv_file/'),
					home_img  = hp.file_processor(hp, request.FILES.get('home_img'), 'home_img', 'home_img/'),
				)
				status = data.save()
				return redirect('all_about')
			
			elif request.method == 'GET':
				return render(request, 'about_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'about_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_about(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			aboutWhere = Q_set(trash=False)
			aboutInfo  = aboutCL.objects.filter(aboutWhere)

			return render(request, 'about_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'aboutData': aboutInfo})
		else:
			return redirect('home')



	def view_about(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			aboutWhere = Q_set(id=id, trash=False)
			aboutInfo  = aboutCL.objects.get(aboutWhere)

			return render(request, 'about_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'aboutData': aboutInfo})
		else:
			return redirect('home')



	def edit_about(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			aboutWhere = Q_set(id=id, trash=False)
			aboutInfo  = aboutCL.objects.get(aboutWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('about_edit'):

				if request.FILES.get('about_img') != None and request.FILES.get('about_img') != '':
					aboutImg = hp.file_processor(hp, request.FILES.get('about_img'), 'about_img', 'about_img/')
				else:
					aboutImg = aboutInfo.about_img

				if request.FILES.get('cv_file') != None and request.FILES.get('cv_file') != '':
					cvFile = hp.file_processor(hp, request.FILES.get('cv_file'), 'about', 'cv_file/')
				else:
					cvFile = aboutInfo.cv_file

				if request.FILES.get('home_img') != None and request.FILES.get('home_img') != '':
					homeImg = hp.file_processor(hp, request.FILES.get('home_img'), 'home_img', 'home_img/')
				else:
					homeImg = aboutInfo.home_img

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = aboutCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					about_txt = request.POST.get('about_txt'),
					about_img = aboutImg,
					cv_file   = cvFile,
					home_img  = homeImg,
			    )
				# Data entry block end
				return redirect('all_about') 

			elif request.method == 'GET':
				return render(request, 'about_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'aboutData': aboutInfo})
			
			return render(request, 'about_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'aboutData': aboutInfo})
		else:
			return redirect('home')



	def delete_about(request, id):
		if request.session.has_key('username'):

			aboutWhere = Q_set(id=id, trash=False)
			aboutInfo  = aboutCL.objects.get(aboutWhere)

			aboutInfo.delete()
			return redirect('all_about')
		else:
			return redirect('home')
