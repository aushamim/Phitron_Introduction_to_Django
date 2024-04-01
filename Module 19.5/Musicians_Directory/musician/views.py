from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from musician.forms import MusicianForm
from musician.models import Musician


# Create your views here.


class AddMusician(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = "musician/add_musician.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        return super().form_valid(form)


class EditMusician(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = "musician/add_musician.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
