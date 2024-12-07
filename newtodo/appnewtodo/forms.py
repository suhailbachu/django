from django import forms

from appnewtodo.models import Todo_data


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo_data
        fields = "__all__"