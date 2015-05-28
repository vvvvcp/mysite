from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text

class Member(models.Model):
    name   = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=10) #N22270
    email  = models.EmailField()

class Vote(models.Model):
    question = models.ForeignKey(Choice)
    member_id = models.ForeignKey(Member)
