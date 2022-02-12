from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Entreprenuer(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, primary_key=True)
    password = models.CharField(max_length=100, blank=False)
    mobileno = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "entreprenuers"


class EntreprenuerContact(models.Model):
    firstname = models.CharField(max_length=100, blank=False)
    lastname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, primary_key=True)
    subject = models.CharField(max_length=100, blank=False)
    query = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = "entreprenuercontact"


class EntreprenuerIdeas(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    mobileno = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    ideaname = models.CharField(max_length=100, blank=False)
    ideadesc = models.CharField(max_length=100, blank=False)
    ideacat = models.CharField(max_length=100, blank=False)
    about = models.CharField(max_length=400, blank=False)
    invmail = models.CharField(max_length=100, blank=False)
    resume = models.FileField(upload_to='files/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        db_table = "entreprenuerideas"
