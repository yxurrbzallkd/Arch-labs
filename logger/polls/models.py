from django.db import models

# Create your models here.
class Entry(models.Model):
    UUID = models.IntegerField()
    msg = models.CharField(max_length=100)
