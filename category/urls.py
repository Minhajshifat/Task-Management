from django.urls import path, include
from . import views


urlpatterns = [
    path("addcategori/", views.add_category, name="addcategory"),
]
