import datetime

from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Mission(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=100000)
    soulswon = models.IntegerField(default=10000)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Widows(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=100000)
    widowsfed = models.IntegerField(default=10000)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

