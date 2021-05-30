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
from apps.backend_apps.booking.models import Cl as bookingCL
from apps.backend_apps.event.models import Cl as eventCL


# Create your views here.
class Booking():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def add_booking(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			# event
			eventWhere = Q_set(status='active', trash=False)
			eventInfo  = eventCL.objects.filter(eventWhere)

			# Add Start Here ------------->
			if request.method == 'POST' and request.POST.get('booking_add'):

				# event
				sineventWhere = Q_set(event_id=request.POST.get('event_id'), status='active', trash=False)
				sineventInfo  = eventCL.objects.get(sineventWhere)

				# Data entry block start 
				data = bookingCL(
					booking_id          = hp.unique_custom_id(hp, 'B'),
					booking_for         = request.POST.get('booking_for'),
					booking_description = request.POST.get('booking_description'),
					booking_remark      = request.POST.get('booking_remark'),
					event_id            = sineventInfo,
				)
				status    = data.save()
				return redirect('all_booking')
			
			elif request.method == 'GET':
				return render(request, 'booking_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'eventData': eventInfo})

			return render(request, 'booking_add.html', {'menuData': menuInfo, 'msgData': msgInfo, 'eventData': eventInfo})
		else:
			return redirect('home')



	def all_booking(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)
			
			bookingWhere = Q_set(trash=False)
			bookingInfo  = bookingCL.objects.filter(bookingWhere)

			return render(request, 'booking_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'bookingData': bookingInfo})
		else:
			return redirect('home')



	def view_booking(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			bookingWhere = Q_set(id=id, trash=False)
			bookingInfo  = bookingCL.objects.get(bookingWhere)

			return render(request, 'booking_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'bookingData': bookingInfo})
		else:
			return redirect('home')



	def edit_booking(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = contactCL.objects.filter(msgWhere)

			bookingWhere = Q_set(id=id, trash=False)
			bookingInfo  = bookingCL.objects.get(bookingWhere)

			# event
			eventWhere = Q_set(status='active', trash=False)
			eventInfo  = eventCL.objects.filter(eventWhere)

			# Update Start Here ------------->
			if request.method == 'POST' and request.POST.get('booking_edit'):

				# event
				sineventWhere = Q_set(event_id=request.POST.get('event_id'), status='active', trash=False)
				sineventInfo  = eventCL.objects.get(sineventWhere)

				# Data entry block start 
				where       = Q_set(id=id, trash=False)
				pre_update  = bookingCL.objects.select_related().filter(where)
				post_update = pre_update.update(
					booking_for         = request.POST.get('booking_for'),
					booking_description = request.POST.get('booking_description'),
					booking_remark      = request.POST.get('booking_remark'),
					status              = request.POST.get('status'),
					event_id            = sineventInfo,
			    )
				return redirect('all_booking')
				# Data entry block end

			elif request.method == 'GET':
				return render(request, 'booking_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'bookingData': bookingInfo, 'eventData': eventInfo})
			
			return render(request, 'booking_edit.html', {'menuData': menuInfo, 'msgData': msgInfo, 'bookingData': bookingInfo, 'eventData': eventInfo})
		else:
			return redirect('home')



	def delete_booking(request, id):
		if request.session.has_key('username'):

			bookingWhere = Q_set(id=id, trash=False)
			bookingInfo  = bookingCL.objects.get(bookingWhere)

			bookingInfo.delete()
			return redirect('all_booking')
		else:
			return redirect('home')
