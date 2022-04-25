from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    price = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title 

