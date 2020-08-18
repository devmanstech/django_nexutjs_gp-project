from django.contrib.auth.models import User
# from json_field import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    # STUDENT = 1
    # TEACHER = 2
    # SUPERVISOR = 3
    # ROLE_CHOICES = (
    #     (STUDENT, 'Student'),
    #     (TEACHER, 'Teacher'),
    #     (SUPERVISOR, 'Supervisor'),
    # )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.TextField(max_length=100, null=True, blank=True)
    talent = models.TextField(max_length=100, null=True, blank=True)
    birthdate = models.CharField(max_length=100, null=True, blank=True)
    hearfrom = models.CharField(max_length=100, null=True, blank=True)
    smiley = models.CharField(max_length=100, null=True, blank=True)
    telegram = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    haha= models.CharField(max_length=100, null=True, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birthdate = models.DateField(null=True, blank=True)
    # role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    print("instance", instance)
    print("sender", sender)
    print("created", created)
    
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
