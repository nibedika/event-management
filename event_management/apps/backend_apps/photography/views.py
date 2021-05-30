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
from apps.backend_apps.photography.models import Cl as photographyCL


# Create your views here.
class Photography():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_photography(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('photography_add'):

				# Data entry block start 
				data = photographyCL(
					photography_id    = hp.unique_custom_id(hp, 'SEI'),
					photography_title = request.POST.get('photography_title'),
					regular_price     = request.POST.get('regular_price'),
					current_price     = request.POST.get('current_price'),
					photography_txt   = request.POST.get('photography_txt'),
					photography_icon  = hp.file_processor(hp, request.FILES.get('photography_icon'), 'photography_icon', 'photography_icon/'),
				)
				status = data.save()
				return redirect('all_photography')
			
			elif request.method == 'GET':
				return render(request, 'photography_add.html', {'menuData': menuInfo, 'msgData': msgInfo})

			return render(request, 'photography_add.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('home')



	def all_photography(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			photographyWhere = Q_set(trash=False)
			photographyInfo  = photographyCL.objects.filter(photographyWhere)

			return render(request, 'photography_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'photographyData': photographyInfo})
		else:
			return redirect('home')



	def view_photography(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			photographyWhere = Q_set(id=id, trash=False)
			photographyInfo  = photographyCL.objects.get(photographyWhere)

			return render(request, 'photography_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'photographyData': photographyInfo})
		else:
			return redirect('home')



	def edit_photography(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			photographyWhere = Q_set(id=id, trash=False)
			photographyInfo  = photographyCL.objects.get(photographyWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('photography_edit'):

				if request.FILES.get('photography_icon') != None and request.FILES.get('photography_icon') != '':
					photographyIcon = hp.file_processor(hp, request.FILES.get('photography_icon'), 'photography_icon', 'photography_icon/')
				else:
					photographyIcon = photographyInfo.photography_icon

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = photographyCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					photography_title = request.POST.get('photography_title'),
					photography_txt   = request.POST.get('photography_txt'),
					regular_price     = request.POST.get('regular_price'),
					current_price     = request.POST.get('current_price'),
					status            = request.POST.get('status'),
					photography_icon  = photographyIcon
			    )
				# Data entry block end
				return redirect('all_photography') 

			elif request.method == 'GET':
				return render(request, 'photography_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'photographyData': photographyInfo})
			
			return render(request, 'photography_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'photographyData': photographyInfo})
		else:
			return redirect('home')



	def delete_photography(request, id):
		if request.session.has_key('username'):

			photographyWhere = Q_set(id=id, trash=False)
			photographyInfo  = photographyCL.objects.get(photographyWhere)

			photographyInfo.delete()
			return redirect('all_photography')
		else:
			return redirect('home')
