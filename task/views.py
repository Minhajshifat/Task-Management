from django.shortcuts import render, redirect
from . import forms
from . import models
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# from django.shortcuts import render
# from rest_framework import viewsets

# # Create your views here.
# from . import models
# from . import serializers


# class taskViewset(viewsets.ModelViewSet):
#     queryset = models.TaskModel.objects.all()
#     serializer_class = serializers.TaskSerializer


# class categoryViewset(viewsets.ModelViewSet):
#     queryset = models.TaskCategory.objects.all()
#     serializer_class = serializers.categorySerializer


# Create your views here.
def add_task(request):
    if request.method == "POST":
        taskform = forms.taskform(request.POST)
        if taskform.is_valid():
            task = taskform.save(commit=False)
            task.user = request.user
            task.save()
            send_mail_to_user(request.user, "Task added successfully", "add_mail.html")

            return redirect("home")
    else:
        taskform = forms.taskform()
    return render(request, "add_task.html", {"form": taskform})


def edit_post(request, id):
    post = forms.TaskModel.objects.get(pk=id)
    taskform = forms.taskform(instance=post)
    if request.method == "POST":
        taskform = forms.taskform(request.POST, instance=post)
        if taskform.is_valid():
            taskform.save()
            if post.complete:
                send_mail_to_user(request.user, "Task completed", "completed.html")
            return redirect("home")
    return render(request, "add_task.html", {"form": taskform})


def delete_post(request, id):
    post = models.TaskModel.objects.get(pk=id)
    post.delete()
    return redirect("showtask")


def show_task(request, category_slug=None):
    user_id = request.user.id

    Tasks = models.TaskModel.objects.filter(user=user_id).order_by("task_due_date")

    category = models.TaskCategory.objects.all()
    if category_slug:
        cat_type = models.TaskCategory.objects.filter(slug=category_slug).first()
        if cat_type:
            Tasks = models.TaskModel.objects.filter(
                category=cat_type, user=user_id
            ).order_by("task_due_date")
    return render(
        request,
        "show_task.html",
        {"Tasks": Tasks, "categories": category},
    )


def tasksort(request):
    user_id = request.user.id
    Tasks = models.TaskModel.objects.filter(user=user_id).order_by("-priority")
    category = models.TaskCategory.objects.all()
    return render(
        request,
        "show_task.html",
        {"Tasks": Tasks, "categories": category},
    )


def send_mail_to_user(user, subject, template):

    message = render_to_string(
        template,
        {
            "user": user,
        },
    )
    send_email = EmailMultiAlternatives(subject, "", to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()
