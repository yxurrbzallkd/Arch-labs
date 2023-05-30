from django.db import models

class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    msg = models.CharField(max_length=100)
