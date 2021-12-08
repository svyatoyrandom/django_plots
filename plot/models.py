from django.core import validators
from django.core.validators import MinValueValidator
from django.db import models

from plot.validators import BracketValidator

def get_plot_path(instance: models.Model):
    return '/plots/{}/{}'.format(instance.id, str(instance.id)  + '.jpeg')

# Create your models here.
class Plot(models.Model):
    start_point = models.FloatField()
    interval = models.FloatField(validators=[MinValueValidator(1e-4),])
    step = models.FloatField(validators=[MinValueValidator(1e-4),])
    plot_function = models.TextField(max_length=200, validators=[BracketValidator(),])
    date_upload = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    plot_image = models.ImageField(upload_to=get_plot_path ,blank=True, null=True)

    def __str__(self):
        return 'f(x) = {}, start point = {}, interval = {} plot image path: {}'.format(self.plot_function, self.start_point, self.interval, self.plot_image)