from django import forms
from .models import Startup


class StartupAddForm(forms.Form):
    name = forms.CharField(label="Add a startup you're interested in", widget=forms.TextInput(
        attrs = {
            "placeholder": "Startup name",
        }))
    latest_funding = forms.DecimalField()
    description = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > 1:
            return name
        else:
            raise(forms.ValidationError("Pick a valid startup name"))

    def clean_latest_funding(self):
        latest_funding = self.cleaned_data.get("latest_funding")
        return latest_funding

class StartupModelForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = [
            "name",
            "latest_funding",
            "description",
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > 1:
            return name
        else:
            raise(forms.ValidationError("Pick a valid startup name"))

    def clean_latest_funding(self):
        latest_funding = self.cleaned_data.get("latest_funding")
        return latest_funding
