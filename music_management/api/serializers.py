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

    def update(self, instance, validated_data):
        instance.song_title = validated_data.get('song_title',instance.song_title)
        instance.album = validated_data.get('album',instance.album)
        instance.artist = validated_data.get('artist',instance.artist)
        instance.audio =validated_data.get('audio',instance.audio)
        instance.save()
        return instance
