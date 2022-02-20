from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class College(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pictures')
    desc = models.TextField()
    fees = models.IntegerField()
    type = models.CharField(max_length=50)
    clgLink = models.CharField(max_length=100)
    courses = ArrayField(models.CharField(max_length=500), blank=True)
    cutOff = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f'{self.name}'