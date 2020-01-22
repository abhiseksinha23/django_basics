from django import forms
from django.core import validators

#def check_for_z(value):
#    if value[0].lower()!='z':
#        raise forms.ValidationError("z is not there")

class FormName(forms.Form):
    name = forms.CharField()  #validators=[check_for_z]
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        clean_all = super().clean()
        email = clean_all['email']
        vmail = clean_all['verify_email']

        if email!=vmail:
            raise forms.ValidationError("Emails not match")
