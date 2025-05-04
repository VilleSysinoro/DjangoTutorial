from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255) # Textfield for the fitst name with maximum of 255 characters
    lastname = models.CharField(max_length=255) # Textfield for the last name with maximum of 255 characters