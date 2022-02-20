from django.db import models
# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    message = models.TextField()
    notification = models.BooleanField()

    def __str__(self):
        return f'{self.name}'