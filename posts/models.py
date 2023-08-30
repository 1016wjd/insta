from django.db import models

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #생성시간
    updated_at = models.DateTimeField(auto_now=True) #수정시간
    image = models.ImageField(upload_to='image/')