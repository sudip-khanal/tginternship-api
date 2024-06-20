from django.db import models

from apps.user.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title},{self.author}"