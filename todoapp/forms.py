from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(attrs = {"class":"myinput", "placeholder":"Enter To-do"}))
    class Meta:
        model = Task
        fields = ["title"]