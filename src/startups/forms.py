from django import forms


class StartupAddForm(forms.Form):
    name = forms.CharField()
    latest_funding = forms.DecimalField()
    description = forms.CharField()
