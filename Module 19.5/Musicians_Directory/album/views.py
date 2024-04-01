from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from album.forms import AlbumForm
from album.models import Album


class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "album/add_album.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super().form_valid(form)


class EditAlbum(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "album/add_album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


class DeleteAlbum(DeleteView):
    model = Album
    template_name = "album/delete_album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
