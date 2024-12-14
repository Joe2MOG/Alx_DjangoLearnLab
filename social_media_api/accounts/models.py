#from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    #followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='users_following_me',
    )
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='users_i_am_following',
        blank=True,
    )
