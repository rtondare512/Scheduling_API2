from django.db import models

# Create your models here.
class DT(models.Model):
	dt=models.DateTimeField()
	url=models.CharField(max_length=55)