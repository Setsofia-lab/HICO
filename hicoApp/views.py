from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from .models import *

def homepage(request):
    return HttpResponse("This is the HICO homepage")

# def blog(request):
#     latest_blogs = Blog.objects.order_by("-pub_date")[:5]
#     output = ",".join([blog.title for blog in latest_blogs])
#     return HttpResponse(output)

def blog(request):
    latest_blogs = Blog.objects.order_by("-pub_date")[:5]
    context = {"latest_blogs": latest_blogs }
    return render(request, "hicoApp/blog.html", context)

def blog_detail (request, blog_id):
    return HttpResponse (" You are looking at HICO blogPost %s." %blog_id)

def mission(request):
    latest_missions = Mission.objects.order_by("-pub_date")[:5]
    context = {"latest_missions": latest_missions }
    return render(request, "hicoApp/mission.html", context)

def mission_detail (request, mission_id):
    return HttpResponse (" You are looking at HICO Mission %s." %mission_id)

def widows(request):
    latest_widows = Widows.objects.order_by("-pub_date")[:5]
    context = {"latest_widows": latest_widows }
    return render(request, "hicoApp/widows.html", context)

def widows_detail (request, widows_id):
    return HttpResponse (" You are looking at HICO Widows Project %s." %widows_id)