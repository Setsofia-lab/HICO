from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import *

def index(request):
    return render(request, "hicoApp/index.html")

# def blog(request):
#     latest_blogs = Blog.objects.order_by("-pub_date")[:5]
#     output = ",".join([blog.title for blog in latest_blogs])
#     return HttpResponse(output)

def blog(request):
    latest_blogs = Blog.objects.order_by("-pub_date")[:5]
    context = {"latest_blogs": latest_blogs }
    return render(request, "hicoApp/blog.html", context)

def blog_detail (request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render (request,  "hicoApp/blog_detail.html", {"blog": blog})

def mission(request):
    latest_missions = Mission.objects.order_by("-pub_date")[:5]
    context = {"latest_missions": latest_missions }
    return render(request, "hicoApp/mission.html", context)

def mission_detail (request, mission_id):
    mission = get_object_or_404(Mission, pk=mission_id)
    return render (request,  "hicoApp/mission_detail.html", {"mission": mission})

def widows(request):
    latest_widows = Widows.objects.order_by("-pub_date")[:5]
    context = {"latest_widows": latest_widows }
    return render(request, "hicoApp/widows.html", context)

def widows_detail (request, widows_id):
    widows = get_object_or_404(Widows, pk=widows_id)
    return render (request,  "hicoApp/widows_detail.html", {"widows": widows})