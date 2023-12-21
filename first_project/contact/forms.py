from django import forms
from .models import contactFrom
class contact_Form(forms.ModelForm):
    class Meta:
        model = contactFrom
        fields = ['usename', 'email', 'body']