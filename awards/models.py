from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=40)
    description = HTMLField()
    date_posted = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200,blank=True)