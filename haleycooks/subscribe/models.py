from django.db import models

# Create your models here.
class Email(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
