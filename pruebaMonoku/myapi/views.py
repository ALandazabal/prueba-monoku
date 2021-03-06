from django.shortcuts import render

from django.http import JsonResponse

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, generics #,filters
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import ArtistSerializer, SongSerializer
from .models import Artist, Genre, Song


class SongFilter(filters.FilterSet):
    #genre_id = filters.ModelChoiceFilter(queryset=Genre.objects.all())
    class Meta:
        model = Song
        #list_display = ['Titulo','Bandas','Subgenero', 'Genero']
        #fields = ['title','bands','subgenre_id','genre_id']
        fields = ['title','bands','subgenre_id']

        """ def __init__(self, *args, **kwargs):
            super(SongFilter, self).__init__(*args, **kwargs)
            self.fields['description'] = 'Something' """

    """ def get_queryset(self, request):
        return super().get_queryset(request).select_related("thing") """


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer

    lookup_field = 'id'

    # Showing a input text to search for a match
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['title']

    # Show two filter fields
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['title','bands','subgenre_id']
    filterset_class = SongFilter



class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    lookup_field = 'id'


""" @api_view(['GET'])
def song_list(request, title):
    """
    #List songs
"""
    song = Song.objects.filter(title=title).first()

    if not song:
        return JsonResponse({"error": "invalid video id"}, status=400)

    serializer = SongSerializer(song)

    return Response(serializer.data, status=status.HTTP_201_CREATED) """
