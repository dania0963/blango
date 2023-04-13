from django.utils import timezone
from operator import mod
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

        author_id=models.IntegerField()
        published_at= models.DateTimeField(default=timezone.now)
        title= models.CharField(max_length=30)
        slug = models.SlugField(unique=True)
        summary=models.CharField(max_length=200) 
        content=models.TextField(max_length=500)