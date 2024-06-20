
from django.db import models
from apps.user.models import User
from apps.book.models import Book

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='in_libraries')
    owner = models.ForeignKey(User, related_name='owned_libraries', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.name},{self.address}"
