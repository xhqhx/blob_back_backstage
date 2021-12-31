from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(models.Model):
    GENDER = (
        ('M', '男'),
        ('F', '女')
    )
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    status = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER,max_length=1,default='M')
    introduction = models.TextField(default='')

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.username


class Friend(models.Model):
    GENDER = (
        ('M', '男'),
        ('F', '女')
    )
    friend_id = models.AutoField(primary_key=True)
    friend_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER,max_length=1,default='M')

    def __str__(self):
        return self.friend_name

    class Meta:
        db_table = "Friend"


class FriendRelationship(models.Model):
    friend_relationship_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    friend = models.ForeignKey(to=Friend,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.friend_relationship_id)

    class Meta:
        db_table = "FriendRelationship"


class Wish(models.Model):
    PERMISSION_TYPE = (
        ('public', '公开'),
        ('private', '私密'),
        ('fans', '仅粉丝可见')
    )
    wish_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    permission = models.CharField(choices=PERMISSION_TYPE, default='public', max_length=8)
    post_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.wish_id)

    class Meta:
        db_table = "Wish"


