import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    auth_key = models.CharField(max_length=10)

    def __str__(self):
    	return self.question_text    

    def get_answers_percentage(self):
        # TODO: Return each answers' percentage based on the votes.
        pass	

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text

    def add_vote(self):
        _votes = self.votes + 1
        self.votes = _votes
        self.save()
        return self.votes
