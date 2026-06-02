from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.FloatField()
    # TODO: Task 2.1 - Movie -> Director relation (ForeignKey on Movie, related_name='movies')
