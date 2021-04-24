from django.contrib import admin

from .models import Song, Album, Artist, Band, Genre, Instrument, Subgenre, Tag

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(Instrument)
admin.site.register(Subgenre)
admin.site.register(Tag)
