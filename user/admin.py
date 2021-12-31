from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Friend, FriendRelationship,  User,Wish
# Register your models here.


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('wish_id', 'author', 'content', 'permission')


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('friend_name','friend_id','gender')


@admin.register(FriendRelationship)
class FriendRelationshipAdmin(admin.ModelAdmin):
    list_display = ('friend_relationship_id','friend','user')




@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'email','password','status','user_id','introduction')

