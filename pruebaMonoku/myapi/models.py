from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200, null=False)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)


class Album(models.Model):
    title = models.CharField(max_length=300, null=False)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Genre(models.Model):
    description = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.description

class Subgenre(models.Model):
    description = models.CharField(max_length=200, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Tag(models.Model):
    description = models.CharField(max_length=200, null=False)


class Instrument(models.Model):
    description = models.CharField(max_length=200, null=False)


class Song(models.Model):

    date = models.CharField(
        max_length=50,
        null=False
    )

    external_id = models.IntegerField(null=True)

    title = models.CharField(
        max_length=256,
        null=False
    )

    duration = models.CharField(
        max_length=256,
        null=False
    )

    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    subgenre = models.ForeignKey(Subgenre, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag)

    instruments = models.ManyToManyField(Instrument)

    bands = models.ManyToManyField(Band)

    def __str__(self):
        return '{} album {} date {}'.format(self.title, self.album, self.date)
