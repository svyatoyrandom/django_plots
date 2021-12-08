from datetime import datetime
from django.forms import ModelForm, widgets
from django.db.models import fields

from plot.models import Plot


class PlotForm(ModelForm):
    # start_point = forms.DecimalField(label='Начальная точка графика', required=True)
    # finish_point = forms.DecimalField(label='Конечная точка графика', required=True)
    # plot_function = forms.CharField(label='Зависимость вида f(x)',max_length=100)
    # step = forms.DecimalField(label='Шаг',min_value=1e-6)
    date_upload = datetime.now()
    class Meta:
        model = Plot
        fields = ['start_point', 'plot_function', 'step', 'interval']
        labels = {
            'start_point': 'Начальная точка графика',
            'plot_function': 'Зависимость вида f(x)',
            'step': 'Шаг',
            'interval': 'Интервал',
        }
        widgets = {
            'plot_function': widgets.TextInput()
        }

