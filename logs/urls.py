""" URLS for the logs app """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.logs, name='logs'),
]
