from django import forms
from phonenumber_field.formfields import PhoneNumberField


class PropertyMessageForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Your name is required'})
    email = forms.EmailField(error_messages={'required': 'Your email is required'})
    phone = PhoneNumberField(error_messages={'required': 'Your phone number is required', 'invalid': 'Enter a valid phone number (e.g. +254727843600).',})
    message = forms.CharField(widget=forms.Textarea, error_messages={'required':'The message is required'})