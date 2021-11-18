from django.db import models

# Create your models here.
class Plot(models.Model):
    interval = models.IntegerField()
    step = models.IntegerField()
    plot_function = models.TextField()