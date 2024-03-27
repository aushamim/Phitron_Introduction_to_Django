from django.db import models

from category.models import Category


# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.TextField()
    task_assign_date = models.DateField()
    categories = models.ManyToManyField(Category)
    is_completed = models.BooleanField(blank=True, default=False)

    def __str__(self) -> str:
        return self.task_title
