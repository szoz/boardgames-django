from rest_framework import serializers

from . import models


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = "__all__"
