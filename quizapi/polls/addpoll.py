from django.db import models
from polls.models import Choice, Question
from django.utils import timezone

class _AddPoll():
	""" 
	Used to add questions.
	add_question: Add a question.
	"""
	def add_question(question, choices, owner):
		check = is_valid(question, choices)

		if check == "QuestionTooLong":
			return "The question provided was too long."
		elif check == "ChoiceTooLong":
			return "The choice provided was too long."

		question = Question(question_text=question, pub_date=timezone.now(), auth_key=owner)
		question.save()

		for choice in choices:
			question.choice_set.create(choice_text=choice, votes=0)

		return True


"""
is_valid: Checks if the information provided
		  for the question is valid.
"""
def is_valid(question, choices):
	if len(question) > 300:
		return "QuestionTooLong"
	elif len([choice for choice in choices if len(choice) < 300]) != len(choices):
		return "ChoiceTooLong"
	return True
