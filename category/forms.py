from django import forms
from .models import TaskCategory
class categoryform(forms.ModelForm):
    class Meta:
        model=TaskCategory
        fields='__all__'