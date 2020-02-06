from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            'title',
            'task',
            'priority',
        ]

        widgets = {
            'task': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
