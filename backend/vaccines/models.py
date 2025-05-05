from django.db import models
# Create your models here.

class Vaccine(models.Model):
    name = models.fields.CharField(unique=True)