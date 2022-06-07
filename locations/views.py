from django.shortcuts import render

def location(request):
    """ A view to return the index page """

    return render(request, 'locations/location.html')