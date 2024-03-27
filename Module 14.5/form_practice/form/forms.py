from django import forms


class basicForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="Date of Birth"
    )
    age = forms.DecimalField(label="Age")
    phone = forms.CharField(
        max_length=11, label="Phone No.", help_text="Enter without +88"
    )
    address = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}), label="Address")
    course = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=[
            ("web-dev", "Web Development"),
            ("app-dev", "App Development"),
            ("front-end", "Front-end Development"),
            ("back-end", "Back-end Development"),
            ("full-stack", "Full Stack Development"),
        ],
        label="Select your desired course",
    )
    extra_course = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[
            ("react", "React JS"),
            ("next", "Next JS"),
            ("redux", "Redux"),
            ("mongodb", "MongoDB"),
            ("sql", "SQL"),
            ("firebase", "Firebase"),
        ],
        label="Select additional courses",
    )
    agree = forms.BooleanField(label="I agree to the terms and conditions")
