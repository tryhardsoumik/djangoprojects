from django import forms
from polls.models import Tasklist

class TaskForm(forms.ModelForm):# the class will talk about which database i'm connecting
    class Meta:
        model=Tasklist# database
        fields=['task','done']# fields of the model

