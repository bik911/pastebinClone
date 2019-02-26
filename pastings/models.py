from django.db import models

# Create your models here.
class Pastings(models.Model):
    txt = models.CharField(max_length=200)
