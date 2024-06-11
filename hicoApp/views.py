from django.http import HttpResponse
from django.template import loader

from .models import Blog

def blog(request):
    latest_blogs = Blog.objects.order_by("-pub_date")[:5]
    template = loader.get_template("blog/blog.html")
    context = {
        "latest_blogs": latest_blogs,
    }
    return HttpResponse(template.render(context, request))

def blog(request):
    return HttpResponse("All Blog Titles go here")

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