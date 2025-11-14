from django.db import models

# Create your models here.
from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.CharField(max_length=300)

    actors = models.ManyToManyField(Actor, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
