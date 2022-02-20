from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Course(models.Model):

    name = models.CharField(max_length=100)
    desc = models.TextField()
    desc2 = models.TextField()
    cost = models.TextField()
    coreSubjects = ArrayField(models.CharField(max_length=500), blank=True)
    universities = ArrayField(models.CharField(max_length=5000), blank=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'