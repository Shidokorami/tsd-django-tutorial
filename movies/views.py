from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(ViewSet):
    def list(self, request):
        # TODO: Task 3.3 - Return all movies serialized with MovieSerializer.
        pass

    def retrieve(self, request, pk=None):
        # TODO: Task 3.5 - Return one movie by pk; HTTP 404 if missing.
        pass
