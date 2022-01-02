from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_is_numeric(value):
    if not value.isnumeric():
        raise ValidationError(
            _('%(value)s is not numeric'),
            params={'value': value},
        )

class ContactMessage(forms.Form):
    name = forms.CharField(
        label='name', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.CharField(
        label='email', 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    phone = forms.CharField(
        label='phone', 
        max_length=10, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[validators.MinLengthValidator(10), validate_is_numeric]
    )
    message = forms.CharField(
        label='message', 
        max_length=1000, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    property_id = forms.CharField(
        label='phone', 
        max_length=10, 
        widget=forms.HiddenInput
    )