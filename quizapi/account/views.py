from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from polls.addpoll import _AddPoll
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class Index(View):
	def get(self, request):
		return HttpResponse("Hey!")

class RegisterUser(View):
	pass

class LoginUser(View):
	pass

class LogoutUser(View):
	pass
