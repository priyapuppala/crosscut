from django import forms
from .models import *


class EntreprenuerForm(forms.ModelForm):
    class Meta:
        model = Entreprenuer
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email'}),
            'mobileno': forms.TextInput(attrs={'placeholder': 'Enter Mobile Number'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter Location'}),
        }
        labels = {
            'fullname': "",
            'password': "",
            'email': "",
            'mobileno': "",
            'location': "",
        }


class EntreprenuerLoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class EntreprenuerContactForm(forms.ModelForm):
    class Meta:
        model = EntreprenuerContact
        fields = "__all__"
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'query': forms.Textarea(attrs={'placeholder': 'Message'}),
        }
        labels = {
            'firstname': "",
            'lastname': "",
            'email': "",
            'subject': "",
            'query': "",
        }


class EntreprenuerIdeasForm(forms.ModelForm):
    class Meta:
        model = EntreprenuerIdeas
        exclude = ('fullname', 'email', 'mobileno', 'location', 'invmail',)
        labels = {
            'about': '',
            'resume': 'Resume and bit of your work',
            'ideacat': "",
            'ideadesc': "",
            'ideaname': "",
        }
        widgets = {
            'about': forms.Textarea(attrs={'placeholder': 'Describe about you and your work towards the startup intiative'}),
            'resume': forms.FileInput(attrs={'placeholder': 'Upload Resume'}),
            'ideacat': forms.TextInput(attrs={'placeholder': 'Enter Business System / Category'}),
            'ideadesc': forms.TextInput(attrs={'placeholder': 'Enter StartUp Description'}),
            'ideaname': forms.TextInput(attrs={'placeholder': 'Enter Idea Name'}),
        }
