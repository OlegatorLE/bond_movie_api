from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    runtime = models.CharField(max_length=100)
    plot = models.TextField()
    poster = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
