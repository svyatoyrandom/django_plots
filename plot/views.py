from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.edit import FormView
from django.views.generic import ListView

import sys

from plot.forms import PlotForm
from plot.models import Plot, get_plot_path
from plot.plotmaker import draw_plot

import datetime

# Create your views here.

def index_view(request):
    form = PlotForm
    all_plots = Plot.objects.all()
    return render(request, 'index.html', context={'form': form, 'plots': all_plots.values()})

# def get_plot_params(request):
#     new_plot = PlotForm(request.POST)
#     if new_plot.is_valid():
#         new_plot = new_plot.save()
#         new_plot.plot_image = get_plot_path(new_plot)
#         draw_plot(new_plot)
#         new_plot.save()
#         return redirect('index')
#     else:
#         request.session['errors'] = new_plot.errors
#         return redirect('index')

class PlotFormView(FormView):
    
    template_name = 'index.html'
    form_class = PlotForm
    success_url = '/'
    
    def form_valid(self, form) -> HttpResponse:
        new_plot = self.form_class(self.request.POST)
        new_plot = new_plot.save()
        new_plot.plot_image = get_plot_path(new_plot)
        draw_plot(new_plot)
        new_plot.save()
        return super().form_valid(form)
    
    def form_invalid(self, form) -> HttpResponse:
        all_plots = Plot.objects.all()
        self.extra_context = {'form' : form, 'plots': all_plots.values()}
        # print(self.extra_context['errors'])
        # self.request.session['errors'] = form.errors
        self.template_name = 'index.html'
        print(self.get_context_data())
        return render(self.request, 'index.html', context=self.get_context_data())
    

