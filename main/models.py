from django.db import models


class Advocate(models.Model):
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics')
    twitter = models.URLField()

    def __str__(self):
        return self.username
