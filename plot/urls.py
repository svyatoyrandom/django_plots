from django.urls import path
from django.urls.resolvers import URLPattern

from .views import index_view

urlpatterns = [
    path('', index_view)
]