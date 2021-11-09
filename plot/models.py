from django.db import models

# Create your models here.
class Plot(models.Model):
    date_update = models.DateField()
    interval = models.IntegerField()
    step = models.IntegerField()
    function = models.TextField()