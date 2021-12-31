from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PersonalArticle, Comment, Collect, SecondaryComment, Praise
# Register your models here.


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('image_id', 'image_name', 'url')
#
#
# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ('video_id', 'video_name', 'url')


@admin.register(SecondaryComment)
class SecondaryCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'user', 'first_comment', 'content', 'post_datetime')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'user', 'article', 'content', 'post_datetime')


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    list_display = ('collect_id', 'user', 'article')


@admin.register(Praise)
class PraiseAdmin(admin.ModelAdmin):
    list_display = ('praise_id', 'user', 'article')


@admin.register(PersonalArticle)
class PersonalArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'article_id', 'author', 'content',
                    'post_datetime',  'read_count')
    exclude = ('read_count',)

    def username(self, obj):
        return obj.author.username
    username.short_description = '用户'
