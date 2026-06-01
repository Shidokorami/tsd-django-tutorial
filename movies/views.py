from rest_framework import viewsets
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ViewSet):
    # TODO: Task 3.3 - Create list method that returns list of the all movies.
    # Hint: Return Response object with data from serializer.
    def list(self, request):
        # queryset = ...
        # serializer = ...
        pass

