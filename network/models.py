from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    amountFollower = models.IntegerField(null=True)
    amountFollowing = models.IntegerField(null=True)


class FollowJoin(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    FollowID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userFollowing")


class Posts(models.Model):
    textBody = models.CharField(max_length=280)
    Likes = models.IntegerField()
    Dislikes = models.IntegerField()
    postUser = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    textBody = models.TextField(max_length=80)
    Likes = models.IntegerField()
    Dislikes = models.IntegerField()
    postID = models.ForeignKey(Posts, on_delete=models.CASCADE)
    postUser = models.ForeignKey(User, on_delete=models.CASCADE)
    

