from django.contrib import admin
from django.urls import path,include
from news import views


def r_path(param, show_article):
    pass


urlpatterns = [
    # path('test/', views.test),
    path('personal_data/', views.personal_data),
    path('article_details/', views.article_details),
    # path('image_details/', views.images_details),
    # path('video_details/', views.video_details),
    path('homepage/', views.homepage),
    path('browse_stories/', views.browse_stories),
    path('search_article/', views.search_article),
    path('comments/', views.comments),
    # path('images_details/', views.images_details),
    path('hot_message/', views.hot_message),
    path('show_article/<int:article_id>', views.show_article),
    path('classification/', views.classification),
    # r_path('^show_article/<int:article_id>/(.*?)$', views.show_article)
    ]
