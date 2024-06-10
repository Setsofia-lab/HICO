from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published")


class Mission(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    soulswon = models.IntegerField
    pub_date = models.DateTimeField("date published")


class Widows(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    widowsfed = models.IntegerField
    pub_date = models.DateTimeField("date published")


