from django.db import models
from polls.models import Choice, Question
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

class HandleUsers():
	""" 
	Class to handle users.
	register: Register a user.
	login: Login a user.
	logout: Logout a user.

	"""

	def register(self, info): 
		check = validate_register_information(info)
		if check == True:
			user = User.objects.create_user(info[0], info[1], info[2])
			return "Success!"
		else:
			return check

	def login(self, info):
		check = validate_login_information(info)
		if check == True:
			user = authenticate(username=info[0], password=info[1])
			if user is not None:
				return "Success!"
			else:
				return "Invalid information."
		else:
			return check

	def logout(self, info):
		# Django doesn't throw an error if the user isn't logged in, hmmm...
		logout(info)
		return "Logged out."


""" Validates the information provided to register a user.
"""
def validate_register_information(info):
	try:
		username = info[0]
		email = info[1]
		password = info[2]
	except:
		return "Missing information in the provided information. Please make sure you're providing a username, an email and a password, in the order they are listed."

	if(len(username) < 3):
		return "The username is too short. Minimum length is 3."
	elif(len(username) > 15):
		return "The username is too long. Maximum length is 15."

	if("@" not in email or "." not in email.split("@")[1]):
		return "Invalid email format."

	if(len(password) < 6):
		return "The password is too short. Minimum length is 6."
	elif(len(password) > 16):
		return "The password is too long. Maximum length is 16."

	return True


""" Validates the information provided to login a user.
"""
def validate_login_information(info):
	try:
		username = info[0]
		password = info[1]
	except:
		return "Missing login information. Please provide your username and your password."

	return True
