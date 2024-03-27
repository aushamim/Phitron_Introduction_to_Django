from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render

from album.forms import AlbumForm
from album.models import Album


# Create your views here.
def add_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("home")
    else:
        album_form = AlbumForm()
    return render(request, "album/add_album.html", {"form": album_form})


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == "POST":
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("home")
    else:
        album_form = AlbumForm(instance=album)
    return render(request, "album/add_album.html", {"form": album_form})


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("home")
