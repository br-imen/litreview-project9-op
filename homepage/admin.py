from django.contrib import admin
from . import models

# Register your models here.
#admin.site.register(models.Ticket)

myModels = [models.Ticket, models.Review]  # iterable list
admin.site.register(myModels)