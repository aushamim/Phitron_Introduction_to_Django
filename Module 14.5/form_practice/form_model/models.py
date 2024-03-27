from django.db import models


# Create your models here.
class basicFormModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    birth_date = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    address = models.TextField()
    course = models.CharField(max_length=100)
    extra_course = models.CharField(max_length=100)
    agree = models.BooleanField()
