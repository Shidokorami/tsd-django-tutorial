from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    # TODO: Task 3.2 - Add a custom field bool 'is_recommended' and related method.
    # It should return True for movies with score that equals at least 7.5.
    # Hint: Name of the method should follow this naming convention get_{field_name}
    is_recommended = serializers.SerializerMethodField()

    # TODO: Task 3.1 - Make serializer return all fields from model (including id).
    # Remember to declare model.
    class Meta:
        model = Movie
        fields = []

    def get_is_recommended(self, obj: Movie) -> bool:
        raise NotImplementedError
