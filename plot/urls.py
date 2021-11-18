from django.urls import path
from django.urls.resolvers import URLPattern

from .views import index_view, get_plot_params

urlpatterns = [
    path('', index_view),
    path('plot_params/', get_plot_params)
]