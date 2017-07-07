from django.db import models

# Create your models here.
class Article(models.Model):
	year = models.PositiveIntegerField()
	month = models.PositiveIntegerField()
	day = models.PositiveIntegerField()