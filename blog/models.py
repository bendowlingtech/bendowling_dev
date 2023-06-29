from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    # add additional fields in here

    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_user', null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_user', null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment', null=True)
    def __str__(self):
        return self.content

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='like_user', null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_like', null=True)
    def __str__(self):
        return self.user.username



