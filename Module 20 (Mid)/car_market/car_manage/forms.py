from django import forms

from car_manage.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["car", "created_on"]
