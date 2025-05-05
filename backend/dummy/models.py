from django.db import models

# Create your models here.
class Dummy(models.Model):
    name = models.fields.CharField(unique=True)

    def __str__(self):
        return self.name