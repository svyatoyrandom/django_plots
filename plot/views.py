from django.shortcuts import render
from django.http import HttpResponse

import sys

from plot.forms import PlotForm


# Create your views here.

def index_view(request):
    form = PlotForm
    return render(request, 'index.html', context={'form': form})

def get_plot_params(request):
    print(request.body)
    print(sys.path)
    return HttpResponse('ok')