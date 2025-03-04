from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    add = models.TextField(default='')
    url = models.CharField(max_length=50, default='x')
    profile = models.ImageField(upload_to="profile_pics/")

    def __str__(self):
        return self.username.username