from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    song_title = serializers.CharField(max_length=100)
    album = serializers.CharField(max_length=50)
    artist = serializers.CharField(max_length=50)
    audio = serializers.FileField(default='')

    def create(self, validated_data):
        return Song.objects.create(**validated_data)