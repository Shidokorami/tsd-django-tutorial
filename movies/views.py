from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ViewSet):
    # TODO: Task 3.3 - Create list method that returns list of the all movies.
    # Hint: Return Response object with data from serializer.
    def list(self, request):
        pass

    # TODO: Task 3.4 - Return a single movie by pk serialized with MovieSerializer.
    # Return HTTP 404 when the movie does not exist.
    # Hint: Use get_object_or_404(Movie, pk=pk)
    def retrieve(self, request, pk=None):
        pass
