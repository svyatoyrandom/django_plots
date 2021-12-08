from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings

from .views import index_view, PlotFormView

urlpatterns = [
    path('', index_view, name='index'),
    path('plot_params/', PlotFormView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)