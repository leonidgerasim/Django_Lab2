from django.db import models

# Create your models here.


class Parameter(models.Model):
    value = models.IntegerField(default=0)
    date = models.TimeField(auto_now=True)
