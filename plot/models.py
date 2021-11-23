from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Plot(models.Model):
    start_point = models.FloatField()
    interval = models.FloatField(validators=[MinValueValidator(1e-4),])
    step = models.FloatField(validators=[MinValueValidator(1e-4),])
    plot_function = models.TextField(max_length=200)
    date_upload = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    plot_image = models.ImageField(blank=True, null=True)