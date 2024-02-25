from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=1024)
    year = models.IntegerField()
    author = models.CharField(max_length=1024)

class Author(models.Model):
    name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)


