from django.db import models

# Create your models here.
class user (models.Model):
    name = models.fields.CharField(max_length = 50)
    password = models.fields.CharField(min_length = 8)