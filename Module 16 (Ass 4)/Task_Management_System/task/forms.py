from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "categories": forms.CheckboxSelectMultiple(),
            "is_completed": forms.RadioSelect(
                choices=[
                    ("True", "True"),
                    ("False", "False"),
                ],
            ),
            "task_assign_date": forms.DateInput(attrs={"type": "date"}),
        }
