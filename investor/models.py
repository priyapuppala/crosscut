from django.db import models


# Create your models here.
class Investor(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, primary_key=True)
    password = models.CharField(max_length=100, blank=False)
    mobileno = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "investors"


class InvestorContact(models.Model):
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, primary_key=True)
    subject = models.CharField(max_length=100, blank=False)
    query = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = "investorcontact"


class InvestorProfile(models.Model):
    fullname = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100,blank=True)
    mobile = models.CharField(max_length=100,blank=True)
    location = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=100,blank=False,primary_key=True)
    qualification = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=100, blank=False)
    aadhar = models.CharField(max_length=100, blank=False)
    history = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)
    about = models.CharField(max_length=400, blank=False)

    class Meta:
        db_table = "investorprofile"


class IdeaLikes(models.Model):
    ideaname = models.CharField(max_length=100,blank=False)
    usermail = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = 'idealikes'
