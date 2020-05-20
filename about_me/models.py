from django.db import models


class About(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	skills = models.CharField(max_length=20)
	image = models.FilePathField(path="static/img")