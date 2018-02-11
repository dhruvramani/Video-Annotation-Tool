from django.db import models
from django.contrib.auth.models import User

class Responses(models.Model):
    username = models.CharField(max_length = 20)
    jsonString = models.CharField(max_length = 1000000000000)

    def __str__(self):
        return self.username