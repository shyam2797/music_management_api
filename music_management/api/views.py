from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Song
from .serializers import SongSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# def song_detail(request , pk):
#     song  = Song.objects.get(id = pk)
#     serializer = SongSerializer(song)
#     return JsonResponse(serializer.data)
#
# def song_list(request):
#     song = Song.objects.all()
#     serializer = SongSerializer(song, many=True)
#     return JsonResponse(serializer.data , safe = False)
@csrf_exempt
def song_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = SongSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'song created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')



