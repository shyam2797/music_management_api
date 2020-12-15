from rest_framework import serializers

class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    song_title = serializers.CharField(max_length=100)
    album = serializers.CharField(max_length=50)
    artist = serializers.CharField(max_length=50)
    audio = serializers.FileField(default='')