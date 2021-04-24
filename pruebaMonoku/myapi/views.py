from django.shortcuts import render

from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import SongSerializer, BandSerializer
from .models import Song, Band


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer


@api_view(['GET'])
def song_list(request, title):
    """
    List songs
    """
    song = Band.objects.filter(title=title).first()

    if not song:
        return JsonResponse({"error": "invalid video id"}, status=400)

    serializer = BandSerializer(song)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
