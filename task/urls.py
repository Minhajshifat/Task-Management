from django.urls import path, include
from . import views

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()  # amader router

# router.register("", views.taskViewset)  # router er antena
# router.register("category/", views.categoryViewset)  # router er antena

urlpatterns = [
    path("addtask/", views.add_task, name="addtask"),
    path("showtask/", views.show_task, name="showtask"),
    path("tasksort/", views.tasksort, name="tasksort"),
    path("edit/<int:id>/", views.edit_post, name="editpost"),
    path("delete/<int:id>", views.delete_post, name="deletepost"),
    path(
        "category_wise/<slug:category_slug>/",
        views.show_task,
        name="category_wise",
    ),
    # path("", include(router.urls)),
]
