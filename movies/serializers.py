from rest_framework import serializers

from movies.models import Model


class ModelApiSerializer(serializers.ModelSerializer):
    # TODO: Task 3.2 - Add bool field is_recommended (True when rating >= 7.5).
    is_recommended = serializers.SerializerMethodField()

    # TODO: Task 3.1 - Serialize all Model fields (including id and parent after task 2.1).
    class Meta:
        model = Model
        fields = []

    def get_is_recommended(self, obj: Model) -> bool:
        raise NotImplementedError
