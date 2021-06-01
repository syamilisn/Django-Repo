"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views
app_name = 'learning_logs'
#urlpatterns contains list of pages that can be requested from the learning_logs app
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]