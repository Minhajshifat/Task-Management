from django.shortcuts import render
from task.models import TaskModel
from category.models import TaskCategory


def home(request, category_slug=None):
    Tasks = TaskModel.objects.all().order_by("task_due_date").values()

    category = TaskCategory.objects.all()
    if category_slug:
        cat_type = TaskCategory.objects.filter(slug=category_slug).first()
        if cat_type:
            Tasks = TaskModel.objects.filter(category=cat_type)
    return render(request, "home.html", {"Tasks": Tasks, "categories": category})
