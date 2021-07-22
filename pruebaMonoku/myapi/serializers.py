import json

from rest_framework import serializers

from .models import Album, Artist, Band, Genre, Song, Subgenre


class AlbumSerializer(serializers.RelatedField):
        
    class Meta:
        model = Album
        fields = (
            'title',
            'band'
        )

    def to_representation(self, value):
        return value.title


class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    songs = serializers.SerializerMethodField()
    total_songs = serializers.SerializerMethodField()
    
    class Meta:
        model = Artist
        fields = (
            'name',
            'band_id',
            'songs',
            'total_songs'
        )

    def get_songs(self, obj):
        band_id = obj.band_id
        #print(band_id)
        if Album.objects.filter(band_id=band_id).exists():
            albums = Album.objects.get(band_id=band_id).id

            list_songs = list(Song.objects.filter(album_id=albums).values('title'))
            print(list_songs)
        else:
            list_songs = []
        #print(albums)
        return list_songs

    def get_total_songs(self, obj):
        band_id = obj.band_id
        #print(band_id)
        if Album.objects.filter(band_id=band_id).exists():
            albums = Album.objects.get(band_id=band_id).id

            list_songs = list(Song.objects.filter(album_id=albums).values('title'))
            print(len(list_songs))
        else:
            list_songs = []
        #print(albums)
        return len(list_songs)


class BandSerializer(serializers.RelatedField):
    
    class Meta:
        model = Band
        fields = (
            'name',
        )

    def to_representation(self, value):
        return value.name


class GenreSerializer(serializers.ModelSerializer):
    
    def to_representation(self, value):
        return value.description

    class Meta:
        model = Genre
        fields = (
            'description'
        )

class SubgenreSerializer(serializers.RelatedField):
    #genres = GenreSerializer(read_only=True, many=True)

    def to_representation(self, value):
        return value.description
    
    class Meta:
        model = Subgenre
        fields = (
            'description',
            'genres'
        )

class SongSerializer(serializers.HyperlinkedModelSerializer):
    #bands = serializers.PrimaryKeyRelatedField(queryset=Band.objects.all(), many=True)
    bands = BandSerializer(read_only=True, many=True)
    subgenre = serializers.SerializerMethodField()
    genre = serializers.SerializerMethodField()
    #genre_id = serializers.SerializerMethodField()

    class Meta:
        model = Song
        fields = (
            'id',
            'title',
            'duration',
            'date',
            'external_id',
            'album_id',
            'bands',
            'subgenre',
            'genre',
            #'genre_id',
        )
        depth = 1

    def get_genre(self, obj):
        #print(self.fields['subgenres'])
        genre_id = Subgenre.objects.get(pk=obj.subgenre_id).genre_id
        
        genre_o = Genre.objects.get(pk=genre_id)
        #print(genre_o.description)
        return genre_o.description

    """ def get_genre_id(self, obj):
        genre_id = Subgenre.objects.get(pk=obj.subgenre_id).genre_id
        genre_o = Genre.objects.get(pk=genre_id)
        return genre_o.id """

    def get_subgenre(self, obj):
        name = Subgenre.objects.get(pk=obj.subgenre_id).description
        return name