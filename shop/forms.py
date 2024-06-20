from django import forms
from .models import ColorModel

class ColorForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={"type":'color'}))

    class Meta:
        model = ColorModel
        fields = "__all__"