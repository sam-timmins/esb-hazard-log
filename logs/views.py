""" Views for the logs app """

from django.shortcuts import render

def logs(request):
    """ A view to return the logs page """

    return render(request, 'logs/logs.html')
