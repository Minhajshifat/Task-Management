from django.shortcuts import render, redirect
from . import forms


# Create your views here.
def add_category(request):
    if request.method == "POST":
        categoryform = forms.categoryform(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect("home")
    else:
        categoryform = forms.categoryform()
    return render(request, "add_category.html", {"form": categoryform})
