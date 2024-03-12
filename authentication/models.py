from django.contrib.auth.models import AbstractUser 

from django.db import models


# user modal.
class CustomUser(AbstractUser):
    username = models.fields.CharField(unique=True, max_length=8)

    USERNAME_FIELD = 'username'
   