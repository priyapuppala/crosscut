from django import forms
from .models import *


class InvestorForm(forms.ModelForm):
    class Meta:
        model = Investor
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


class InvestorLoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class InvestorContactForm(forms.ModelForm):
    class Meta:
        model = InvestorContact
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


class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = (
        'username', 'qualification', 'designation', 'company', 'aadhar', 'history', 'category', 'about',)
        labels = {
            'username': 'Username',
            'qualification': "Qualification",
            'designation': "Designation",
            'company': "Company",
            'aadhar': "Aadhar Number",
            'history': "Previous Investments",
            'category': "Looking For",
            'about': "About Yourself",
        }
        widgets = {
            'about': forms.Textarea(attrs={'placeholder': 'About Your Interests'}),
        }


class InvestorApprovalForm(forms.Form):
    atime = forms.CharField(max_length=100)
    adate = forms.CharField(max_length=100)
    feedback = forms.CharField(max_length=400)
    labels = {
        'atime': 'Time',
        'adate': 'Date',
        'feedback': 'Feedback',
    }
    widgets = {
        'feedback': forms.Textarea(attrs={'placeholder': 'Feedback Regarding The StartUp Idea and Your Suggestions'}),
        'adate': forms.DateInput(attrs={'placeholder': 'Date'}),
        'atime': forms.TimeField(),
    }
