from django import forms

from uiapp.models import Mode_data


class ModeForm(forms.ModelForm):
    class Meta:
        model = Mode_data
        fields = "__all__"