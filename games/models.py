from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, unique=True)
    description = models.TextField()


class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    url = models.CharField(max_length=100, unique=True)
    description = models.TextField()
