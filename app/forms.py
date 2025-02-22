from django import forms
from .models import Contact

class Contacts_form (forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Photo', 'Name', 'Surname', 'Phone', 'Email']

