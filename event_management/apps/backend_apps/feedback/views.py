# Buildin Package
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q as Q_set
from package.helper import Helper as hp

# App's Model Import
from apps.access_apps.access.models import User as userDB
from apps.backend_apps.feedback.models import Cl as feedbackCL
from apps.backend_apps.event.models import Cl as eventDB


# Create your views here.
class Feedback():

	def __init__(self, arg):
		super(self).__init__()
		self.arg = arg



	def all_feedback(request):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = feedbackCL.objects.filter(msgWhere)
			
			feedbackWhere = Q_set(trash=False)
			feedbackInfo  = feedbackCL.objects.filter(feedbackWhere)

			return render(request, 'feedback_all.html', {'menuData': menuInfo, 'msgData': msgInfo, 'feedbackData': feedbackInfo})
		else:
			return redirect('home')



	def view_feedback(request, id):
		if request.session.has_key('username'):

			# COMMON INFO FETCHING START
			sessionUsername = request.session['username']
			userWhere       = Q_set(username=sessionUsername)
			menuInfo        = userDB.objects.get(userWhere)

			msgWhere = Q_set(status='unseen', trash=False)
			msgInfo  = feedbackCL.objects.filter(msgWhere)

			feedbackWhere = Q_set(id=id, trash=False)
			feedbackInfo  = feedbackCL.objects.get(feedbackWhere)

			return render(request, 'feedback_view.html', {'menuData': menuInfo, 'msgData': msgInfo, 'feedbackData': feedbackInfo})
		else:
			return redirect('home')



	def delete_feedback(request, id):
		if request.session.has_key('username'):

			feedbackWhere = Q_set(id=id, trash=False)
			feedbackInfo  = feedbackCL.objects.get(feedbackWhere)

			feedbackInfo.delete()
			return redirect('all_feedback')
		else:
			return redirect('home')
