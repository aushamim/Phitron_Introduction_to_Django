from django.shortcuts import render

from album.models import Album
from musician.models import Musician


def home(request):
    musicianData = Musician.objects.all()
    albumData = Album.objects.all()
    return render(
        request, "home.html", {"musicianData": musicianData, "albumData": albumData}
    )
