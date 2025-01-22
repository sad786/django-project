from django.db import models
from datetime import datetime

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    timing  = models.DateTimeField('Date Published')


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    

