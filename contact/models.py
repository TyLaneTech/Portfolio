from django.db import models
from django import forms

class Message(models.Model):
	name= models.CharField(max_length=300)
	email= models.CharField(max_length=300)
	message= models.TextField()