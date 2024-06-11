from django.urls import path

from . import views

urlpatterns = [
    path("blog", views.blog, name="blog"),
    path("<int:blog_id>/blog_detail/", views.blog_detail, name="blog_detail"),
    path("<int:blog_id>/blog_results/", views.blog_results, name="blog_results"),

    path("mission", views.mission, name="mission"),
    path("<int:mission_id>/", views.mission_detail, name="mission_detail"),

    path("widows", views.widows, name="widows"),
    path("<int:widows_id>/", views.widows_detail, name="widows_detail"),
]