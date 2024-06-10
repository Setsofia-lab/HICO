from django.http import HttpResponse


def index(request):
    return HttpResponse("HICO APP UI goes here")
