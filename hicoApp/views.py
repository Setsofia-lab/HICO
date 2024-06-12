from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render

from .models import Blog

def homepage(request):
    return HttpResponse("This is the HICO homepage")

# def blog(request):
#     latest_blogs = Blog.objects.order_by("-pub_date")[:5]
#     output = ",".join([blog.title for blog in latest_blogs])
#     return HttpResponse(output)

def blog(request):
    latest_blogs = Blog.objects.order_by("-pub_date")[:5]
    context = {"latest_blogs": latest_blogs,}
    return render(request, "hicoApp/blog.html", context)

# def blog(request):
#     return HttpResponse("All Blog Titles go here")

def blog_detail (request, blog_id):
    return HttpResponse (" You are looking at HICO blogPost %s." %blog_id)

def blog_results(request, blog_id):
    response = "This is the blog title and contents on blog %s "
    return HttpResponse(response % blog_id)

def mission(request):
    return HttpResponse("All Mission Titles go here")

def mission_detail (request, mission_id):
    return HttpResponse (" You are looking at HICO Mission %s." %mission_id)

def widows(request):
    return HttpResponse("All Widows donations projects go here")

def widows_detail (request, widows_id):
    return HttpResponse (" You are looking at HICO Widows Project %s." %widows_id)