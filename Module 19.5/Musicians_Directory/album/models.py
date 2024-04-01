from django.db import models

from musician.models import Musician


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField(null=True, blank=True)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.album_name
