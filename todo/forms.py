from django import forms 
from .models import todolist

class todoform(forms.ModelForm):
    class Meta:
        model = todolist
        fields = ['todoname','tododesc']
        widgets={
            'todoname':forms.TextInput(attrs={'class':'border border-black p-2 w-[300px]'}),
            'tododesc':forms.Textarea(attrs={'class':'border border-black p-1 w-[300px]'}),
        }
