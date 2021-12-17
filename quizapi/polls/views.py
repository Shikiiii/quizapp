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
		return HttpResponse("probably the main get for polls")

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class AddPoll(View):
	
	def get(self, request):
		return HttpResponse("get information (?)")

	def post(self, request):
		question = request.POST.get("question")
		choices = [choice for choice in request.POST.get("choices")]
		# "auth" is a temporary auth key to know who owns a poll. Default is 0.
		owner = request.POST.get("auth")

		check = _AddPoll.add_question(question, choices, owner)
		return HttpResponse("Your question has been added.") if check == True else check



@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class VotePoll(View):
	
	def get(self, request):
		return HttpResponse("get the votes for a poll (?)")

	def post(self, request):
		question = request.POST.get("question")
		option = request.POST.get("choice")

		check = _VotePoll.add_question(question, option)
		return HttpResponse("You have succesfully voted.") if check == True else check
