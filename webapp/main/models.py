from django.db import models
from django.contrib.auth.models import User

class Responses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    jsonString = models.CharField(max_length = 1000000000000)
    lastId = models.IntegerField()
    gotoId = models.IntegerField()

    def __str__(self):
        return self.user.username 