from django import forms
from .models import enquire_now


class SubmitForm(forms.Form):
    class Meta:
        model=enquire_now
        fields="__all__"




# class LocationField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super(LocationField, self).__init__(*args, **kwargs)
#         self.widget = forms.TextInput(attrs={'class': 'location-input'})