from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
# Create your models here.

class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500,500],
        crop=['middle', 'center'],
        upload_to='profile',
    )
# post_set =  >> 사용자가 올린 게시물들의 모임
# like_posts =  >> 사용자가 누른 좋아요의 모임