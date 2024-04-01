from django import forms

from album.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ["release_date"]

    def clean_rating(self):
        val = self.cleaned_data["rating"]
        print(val)
        if val < 1 or val > 5:
            raise forms.ValidationError("Rating should be within 1 and 5")
        return val
