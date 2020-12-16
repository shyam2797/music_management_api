from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Song
from .serializers import SongSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def song_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            song = Song.objects.get(id = id)
            serializer = SongSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        song = Song.objects.all()
        serializer = SongSerializer(song , many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = SongSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        song  = Song.objects.get(id = id)
        serializer  = SongSerializer(song,data = python_data , partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data  = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream =  io.BytesIO(json_data)
        python_data  =  JSONParser().parse(stream)
        id  = python_data.get('id')
        song  = Song.objects.get(id = id)
        song.delete()
        res = {'msg':'Song Deleted !'}
        return JsonResponse(res ,safe=False)


