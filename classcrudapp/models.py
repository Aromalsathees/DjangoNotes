from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    desc = models.TextField(max_length=50)
    image = models.ImageField(upload_to='book_images/classcrud')

    def __str__(self):
        return self.title