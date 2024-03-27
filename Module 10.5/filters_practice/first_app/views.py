import datetime
from django.shortcuts import render


# Create your views here.
def home(request):
    d = {
        "author": "rahim",
        "intro": "I'm Rahim",
        "age": 20,
        "time": datetime.datetime.now(),
        "comment_date": datetime.datetime(2024, 3, 14, 15, 8, 24, 00000),
        "lst": ["A", "B", "C"],
        "courses": [
            {"id": 1, "name": "Python", "fees": 5000},
            {"id": 2, "name": "Django", "fees": 10000},
            {"id": 3, "name": "CPP", "fees": 9200},
        ],
    }
    return render(request, "first_app/index.html", d)
