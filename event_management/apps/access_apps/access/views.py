# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from package.helper import Helper as hp
from django.db.models import Q as Q_set
import time

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.contact.models import Cl as contactCL
from apps.backend_apps.about.models import Cl as aboutDB
from apps.backend_apps.event.models import Cl as eventDB
from apps.backend_apps.service.models import Cl as serviceDB
from apps.backend_apps.booking.models import Cl as bookingDB
from apps.backend_apps.photography.models import Cl as photographyDB
from apps.backend_apps.package.models import Cl as packageDB
from apps.backend_apps.feedback.models import Cl as feedbackCL


# Create your views here.
class Access():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def sign_up(request):
		if request.method == 'POST' and request.POST.get('sign_up'):

			data = userDB(
				user_id        = hp.unique_custom_id(hp, 'U'),
				name           = request.POST.get('name'),
				username       = request.POST.get('username'),
				email          = request.POST.get('email'),
				password       = request.POST.get('password'),
				confirmed_pass = request.POST.get('confirmed_pass'),
				designation    = 'owner',
			)

			# Username and Email existance check start
			username     = request.POST.get('username')
			email        = request.POST.get('email')
			usernameCond = Q_set(username=username)
			usernameCond = Q_set(email=email)

			usernameExists = False
			emailExists    = False

			if userDB.objects.filter(usernameCond).exists():
				usernameExists = True
			else:
				usernameExists = False

			if userDB.objects.filter(usernameCond).exists():
				emailExists = True
			else:
				emailExists = False

			if usernameExists == False and emailExists == False:
				status = data.save()
				return redirect('sign_in')
			else:
				pass

		elif request.method == 'GET':
			return render(request, 'sign_up.html')
		return render(request, 'sign_up.html')



	def sign_in(request):
		if request.method == 'POST' and request.POST.get('sign_in'):
			loginUsername = request.POST.get('username')
			loginPassword = request.POST.get('password')

			userWhere     = Q_set(username=loginUsername)

			userExixtance = True
			if userDB.objects.filter(userWhere).exists():
				usernameExists = True
			else:
				usernameExists = True

			if userExixtance == True:
				where    = Q_set(username=loginUsername)
				userInfo = userDB.objects.filter(where)

				if userInfo[0].designation == "owner":
					if userInfo[0].username == loginUsername and userInfo[0].confirmed_pass == loginPassword:
						request.session['username'] = loginUsername
						return redirect('home')
					else:
						return redirect('sign_up')
				else:
					return redirect('sign_up')
			else:
				return redirect('sign_up')
		elif request.method == 'GET':
			return render(request, 'sign_in.html')



	def home(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername      = request.session['username']
			userWhere            = Q_set(username=sessionUsername)
			menuInfo             = userDB.objects.get(userWhere)
			
			msgWhere             = Q_set(status='unseen', trash=False)
			msgInfo              = contactCL.objects.filter(msgWhere)
			
			eventWhere           = Q_set(trash=False)
			eventInfo            = eventDB.objects.filter(eventWhere)
			event                = eventInfo.count()
			
			bookingWhere         = Q_set(trash=False)
			bookingInfo          = bookingDB.objects.filter(bookingWhere)
			booking              = bookingInfo.count()
			
			activeBookingWhere   = Q_set(status='active', trash=False)
			activeBookingInfo    = bookingDB.objects.filter(activeBookingWhere)
			activeBooking        = activeBookingInfo.count()
			
			inactiveBookingWhere = Q_set(status='inactive', trash=False)
			inactiveBookingInfo  = bookingDB.objects.filter(inactiveBookingWhere)
			inactiveBooking      = inactiveBookingInfo.count()
			
			serviceWhere         = Q_set(trash=False)
			serviceInfo          = serviceDB.objects.filter(serviceWhere)
			service              = serviceInfo.count()
			
			photographyWhere     = Q_set(trash=False)
			photographyInfo      = photographyDB.objects.filter(photographyWhere)
			photography          = photographyInfo.count()
			
			packageWhere         = Q_set(trash=False)
			packageInfo          = packageDB.objects.filter(packageWhere)
			package              = packageInfo.count()
			
			feedbackWhere        = Q_set(trash=False)
			feedbackInfo         = feedbackCL.objects.filter(feedbackWhere)
			feedback             = feedbackInfo.count()

			return render(request, 'home.html', {'menuData': menuInfo, 'msgData': msgInfo, 'event': event, 'booking': booking, 'activeBooking': activeBooking, 'inactiveBooking': inactiveBooking, 'service': service, 'photography': photography, 'package': package, 'feedback': feedback})
		else:
			return redirect('sign_out')



	def sign_out(request):
		if request.session.has_key('username'):
			try:
				sessionUsername = request.session['username']
				userWhere       = Q_set(username=sessionUsername)
				menuInfo        = userDB.objects.get(userWhere)

				del request.session['username']
				return redirect('sign_up')
			except:
				return redirect('sign_up')
		else:
			return redirect('sign_up')
		return render(request, 'sign_up.html')



	def view_profile(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			return render(request, 'view_profile.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('sign_out')



	def edit_profile(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# Update Profile Picture And Cover Picture Start Here ------------->
			if request.method == 'POST' and request.POST.get('edit_profile'):

				username = request.session['username']

				if request.FILES.get('profile_picture') != None and request.FILES.get('profile_picture') != '':
					profileImage = hp.file_processor(hp, request.FILES.get('profile_picture'), 'pro_pic', 'profile_img/')
				else:
					profileImage = menuInfo.profile_picture

				# Data entry block start 
				where  = Q_set(username=username)
				pre_update = userDB.objects.select_related().filter(where)
				post_update = pre_update.update(
					name            = request.POST.get('name'),
					password        = request.POST.get('password'),
					confirmed_pass  = request.POST.get('confirmed_pass'),
					profile_picture = profileImage
			    )
				# Data entry block end 

				return redirect('view_profile')
			elif request.method == 'GET':
				return render(request, 'edit_profile.html', {'menuData': menuInfo, 'msgData': msgInfo})
			# Update Profile Picture And Cover Picture End Here --------------->

			return render(request, 'edit_profile.html', {'menuData': menuInfo, 'msgData': msgInfo})
		else:
			return redirect('sign_out')



	def delete_profile(request, reUser):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			menuInfo.delete()
			return redirect('sign_out')
		else:
			return redirect('sign_out')






	def web_home(request):

		userWhere        = Q_set(status="active", trash=False)
		menuInfo         = userDB.objects.filter(userWhere).last()
		
		aboutWhere       = Q_set(trash=False)
		aboutInfo        = aboutDB.objects.filter(aboutWhere).last()
		
		serviceWhere     = Q_set(status='active', trash=False)
		serviceInfo      = serviceDB.objects.filter(serviceWhere)
		
		photographyWhere = Q_set(status='active', trash=False)
		photographyInfo  = photographyDB.objects.filter(photographyWhere)
		
		eventWhere       = Q_set(status='active', trash=False)
		eventInfo        = eventDB.objects.filter(eventWhere)
		
		packageWhere     = Q_set(status='active', trash=False)
		packageInfo      = packageDB.objects.filter(packageWhere)
		
		feedbackWhere    = Q_set(trash=False)
		feedbackInfo     = feedbackCL.objects.filter(feedbackWhere)

		# Add Start Here ------------->
		if request.method == 'POST' and request.POST.get('feedback_add'):

			eWhere        = Q_set(id=request.POST.get('event'), status='active', trash=False)
			eInfo         = eventDB.objects.get(eWhere)

			# Data entry block start 
			data = feedbackCL(
				feedback_id = hp.unique_custom_id(hp, 'FI'),
				name        = request.POST.get('name'),
				contact     = request.POST.get('contact'),
				email       = request.POST.get('email'),
				event       = eInfo,
				description = request.POST.get('description'),
				rating      = request.POST.get('rating')
			)
			status = data.save()
			return redirect('web_home')
		else:
			pass
		# Add End Here ------------->

		return render(request, 'website.html', {'active': 'home', 'menuData': menuInfo, 'aboutData': aboutInfo, 'serviceData': serviceInfo, 'photographyData': photographyInfo, 'eventData': eventInfo, 'packageData': packageInfo, 'feedbackData': feedbackInfo})
