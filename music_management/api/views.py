from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse
# Create your views here.

def song_detail(request , pk):
    song  = Song.objects.get(id = pk)
    serializer = SongSerializer(song)
    return JsonResponse(serializer.data)

def song_list(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    return JsonResponse(serializer.data , safe = False)


