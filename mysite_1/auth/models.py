from django.db import models


class RegNumber(models.Model):
	user = models.CharField(max_length=30, primary_key=True)
	number = models.FloatField()
