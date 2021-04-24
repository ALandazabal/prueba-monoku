from rest_framework import serializers

from .models import Song, Album, Band


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = (
            'title',
            'duration',
            'date',
            'album',
        )


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = (
            'title',
            'artist'
        )


class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
        fields = (
            'name'
        )
