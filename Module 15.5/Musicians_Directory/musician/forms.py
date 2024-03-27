from django import forms

from musician.models import Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"
        widgets = {
            "instrument_type": forms.RadioSelect(
                choices=[
                    ("Guiter", "Guiter"),
                    ("Bass", "Bass"),
                    ("Drums", "Drums"),
                    ("Piano", "Piano"),
                    ("Violin", "Violin"),
                ],
            )
        }
        help_texts = {"phone_no": "Enter without +88"}

    def clean_phone_no(self):
        val = self.cleaned_data["phone_no"]
        if len(val) > 11:
            raise forms.ValidationError("Invalid Phone No")
        return val
