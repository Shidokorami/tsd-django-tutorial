from django.db import models


class ParentModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()


class Model(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.FloatField()
    # TODO: Task 2.1 - Add ForeignKey from Model to ParentModel (related_name='models')
