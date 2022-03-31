from django import forms
from django.forms import NumberInput

from salem.widget import TimePickerInput

enthusiastChoices = (
    ("1", "JDM"),
    ("2", "USDM"),
    ("3", "EDM"),
)


class setupMeetInfo(forms.Form):
    latitude = forms.FloatField(
        max_value=999.999,
        widget=forms.HiddenInput(attrs={'id': 'lat'}))
    longitude = forms.FloatField(
        max_value=99.999,
        widget=forms.HiddenInput(attrs={'id': 'lng'}))
    hostName = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name or car club name'}))
    meetPlace = forms.CharField(
        label='Location',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Use the Map to Find Your Location'}))
    meetAddress = forms.CharField(
        label='Address',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Map will Auto-Fill the Address'}))
    meetDescription = forms.CharField(
        label='Description',
        # max_length=100,
        widget=forms.Textarea(attrs={'placeholder': 'Examples: Meet at north end of lot, No-Burnouts, Etc..'}))
    meetDate = forms.DateField(
        label='Meet Date',
        widget=NumberInput(attrs={'type': 'date'}))
    startTime = forms.TimeField(widget=TimePickerInput)
    endTime = forms.TimeField(widget=TimePickerInput)
    enthusiastType = forms.ChoiceField(
        label='Enthusiast Type',
        choices=enthusiastChoices,
        widget=forms.CheckboxSelectMultiple)
