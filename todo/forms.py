from django import forms 
from .models import todolist

class todoform(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['todoname','tododesc']