from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    content = models.TextField()
    keyword = models.CharField(max_length=100)
