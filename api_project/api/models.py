from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    author = models.CharField(max_length=255)  # Book author

    def __str__(self):
        return self.title  # String representation of the model