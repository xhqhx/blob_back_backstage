from django.db import models
from user.models import User
# Create your models here.


# class Image(models.Model):
#     image_id = models.AutoField(primary_key=True)
#     image_name = models.CharField(max_length=100, verbose_name='图片名称')
#     url = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.image_name
#
#     class Meta:
#         db_table = "Image"
#
#
# class Video(models.Model):
#     video_id = models.AutoField(primary_key=True)
#     video_name = models.CharField(max_length=100, verbose_name='视频名称')
#     url = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.video_name
#
#     class Meta:
#         db_table = "Video"


class PersonalArticle(models.Model):
    CATEGORY_TYPE = (
        ('H', '前线热线'),
        ('Z', '疫情实事'),
        ('X', '国际疫情事件'),
    )
    ARTICLE_TYPE = (
        ('I', '图片'),
        ('V', '视频'),
        ('C', '纯文本'),
    )
    article_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200, verbose_name='图片地址', null=True, blank=True)
    video_url = models.CharField(max_length=200, verbose_name='视频地址', null=True, blank=True)
    # image = models.ForeignKey(to=Image, on_delete=models.CASCADE)
    # video = models.ForeignKey(to=Video, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(choices=CATEGORY_TYPE, max_length=1, default='Z')
    article_type = models.CharField(choices=ARTICLE_TYPE, max_length=1, default='C')
    post_datetime = models.DateTimeField(auto_now=True)
    read_count = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "PersonalArticle"


class Collect(models.Model):
    collect_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models.ForeignKey(to=PersonalArticle, on_delete=models.CASCADE)
    isCollect = models.BooleanField(default=True)

    def __str__(self):
        return str(self.collect_id)

    class Meta:
        db_table = "Collect"


# 点赞
class Praise(models.Model):
    praise_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models.ForeignKey(to=PersonalArticle, on_delete=models.CASCADE)
    isPraise = models.BooleanField(default=True)

    def __str__(self):
        return str(self.praise_id)

    class Meta:
        db_table = "Praise"


# 评论表
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    article = models.ForeignKey(to=PersonalArticle, on_delete=models.CASCADE)
    content = models.TextField()
    post_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment_id)

    class Meta:
        db_table = "Comment"


# 二级评论
class SecondaryComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    first_comment = models.ForeignKey(to=Comment,on_delete=models.CASCADE)
    content = models.TextField()
    post_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.comment_id)

    class Meta:
        db_table = "SecondaryComment"


class BrowsingHistory(models.Model):
    browsinghistory_id = models.AutoField(primary_key=True)
    browsing_datetime = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(to=PersonalArticle,on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.browsinghistory_id)

    class Meta:
        db_table = "BrowsingHistory"
