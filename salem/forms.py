from django import forms


enthusiastChoices =(
    ("1", "JDM"),
    ("2", "USDM"),
    ("3", "EDM"),
    ("4", "ALL"),
)

class setupMeetInfo(forms.Form):
    latitude = forms.FloatField(
        max_value=999.999,
        widget=forms.HiddenInput(attrs={'id': 'lat'}))
    longitude = forms.FloatField(
        max_value=99.999,
        widget=forms.HiddenInput(attrs={'id': 'lng'}))
    hostName = forms.CharField(
        label='Your Name',
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'hostName'}))
    meetPlace = forms.CharField(
        label='Location',
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'meetPlace'}))
    meetAddress = forms.CharField(
        label='Address',
        max_length=100,
        widget=forms.TextInput(attrs={'id': 'meetAddress'}))
    startTime = forms.TimeInput()
    endTime = forms.TimeInput()
    enthusiastType = forms.MultipleChoiceField(choices= enthusiastChoices)
