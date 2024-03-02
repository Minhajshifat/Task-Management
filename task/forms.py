from django import forms
from .models import TaskModel


class taskform(forms.ModelForm):
    task_due_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = TaskModel
        exclude = ["user", "task_assigned_date"]
