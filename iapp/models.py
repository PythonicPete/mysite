from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    youremail = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.CharField(max_length=300)
