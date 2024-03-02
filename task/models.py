from django.db import models
from django.utils import timezone
from category.models import TaskCategory
from django.contrib.auth.models import User

PRIORITI_LEVELS = [
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
    (6, "6"),
    (7, "7"),
    (8, "8"),
]


# Create your models here.
class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    task_title = models.CharField(max_length=100)
    describtion = models.TextField(max_length=300)
    complete = models.BooleanField(default=False)
    category = models.ManyToManyField(TaskCategory)
    task_assigned_date = models.DateTimeField(default=timezone.now)
    task_due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITI_LEVELS, null=True, blank=True)

    def __str__(self):
        return self.task_title
