from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clgName = models.TextField()
    course = models.CharField(max_length=50)
    backlogs = models.CharField(max_length=2)
    ugMarks = models.CharField(max_length=4) #Under Graduate Marks(CGPA)
    examName = models.CharField(max_length=20)
    examScore = models.CharField(max_length=6)
    experience = models.CharField(max_length=15)
    paperLevel = models.CharField(max_length=15)
    isProfile = models.BooleanField()
    score = models.FloatField(max_length=10)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()