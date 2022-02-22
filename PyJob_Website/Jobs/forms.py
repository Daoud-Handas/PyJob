from django import forms


class EmailForm(forms.Form):
    your_email = forms.EmailField(label='Your email', max_length=100)
    your_name = forms.CharField(label='Your name', max_length=100, required=False)
