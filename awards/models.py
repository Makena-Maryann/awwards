from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=40)
    description = HTMLField()
    date_posted = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200,blank=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


    @classmethod
    def get_projects(cls):
        all_projects = cls.objects.all()
        return all_projects 

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project 

    def __str__(self):
        return self.title   

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='pics/')
    bio = HTMLField(blank=True,default='I am a new user!') 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
          