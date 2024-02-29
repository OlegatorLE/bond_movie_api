from rest_framework import serializers
from .models import Movie, Actor


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"
