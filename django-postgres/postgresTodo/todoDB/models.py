import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    class Meta:
        db_table = 'questions'
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
        
    # Si ha sido publicado en las últimas 24 horas
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    class Meta:
        db_table = 'choices'
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text