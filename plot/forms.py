from django import forms


class PlotForm(forms.Form):
    start_point = forms.DecimalField(label='Начальная точка графика', required=True)
    finish_point = forms.DecimalField(label='Конечная точка графика', required=True)
    plot_function = forms.CharField(label='Зависимость вида f(x)',max_length=100)
    step = forms.DecimalField(label='Шаг',min_value=1e-6)

