from rest_framework import serializers

from .models import Song, Album, Band


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = (
            'title',
            'artist'
        )


class BandSerializer(serializers.RelatedField):
    
    def to_representation(self, value):
        return value.name
    
    class Meta:
        model = Band
        fields = (
            'name'
        )


class SongSerializer(serializers.HyperlinkedModelSerializer):
    #bands = serializers.PrimaryKeyRelatedField(queryset=Band.objects.all(), many=True)
    bands = BandSerializer(read_only=True, many=True)

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
        )