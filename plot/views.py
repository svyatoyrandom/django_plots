from django.shortcuts import render, redirect
from django.http import HttpResponse

import sys

from plot.forms import PlotForm
from plot.models import Plot


# Create your views here.

def index_view(request):
    form = PlotForm
    all_plots = Plot.objects.all()
    return render(request, 'index.html', context={'form': form, 'plots': all_plots.values()})

def get_plot_params(request):
    new_plot = PlotForm(request.POST)
    new_plot.save()
    return redirect('index')