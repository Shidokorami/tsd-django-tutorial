from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # TODO: Task 3.2 - Add bool field is_recommended (True when rating >= 7.5).
    is_recommended = serializers.SerializerMethodField()

    # TODO: Task 3.1 - Serialize all Movie fields (including id and director after task 2.1).
    class Meta:
        model = Movie
        fields = []

    def get_is_recommended(self, obj: Movie) -> bool:
        raise NotImplementedError
