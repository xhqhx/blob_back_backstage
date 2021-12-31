from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from news.models import PersonalArticle, Collect, Praise, Comment, SecondaryComment, BrowsingHistory
from user.models import User, Friend, FriendRelationship, Wish
from django.template.loader import get_template
from datetime import datetime
from django.forms.models import model_to_dict


# Create your views here.

# 首页
def homepage(request):

    articles = PersonalArticle.objects.all().values()

    if articles:
        return JsonResponse({
            'data': list(articles),
        })
    else:
        return JsonResponse({
            'messages': '没有文章！'
        })


# 热点事迹
def hot_message(request):
    # articles = PersonalArticle.objects.filter(post_datetime=datetime.now()).values()
    articles = PersonalArticle.objects.order_by('-post_datetime')[:10].values()
    return JsonResponse({
        'data': list(articles)
    })
# --------------------------------------------------------------悬浮导航


# 分类查看
def classification(request):
    articles = PersonalArticle.objects.all().values()
    return JsonResponse({
        'article': list(articles),
    })


# -------------------------------------------------------


# 导航点击



# 查看文章
def show_article(request, article_id):
    articles = PersonalArticle.objects.filter(article_id=article_id).values()
    comment = Comment.objects.filter(article_id=article_id).values()
    return JsonResponse({
        'message': list(articles),
        'data': list(comment),
    })


# ----------------------------------------------------


# 个人信息页下的个人详细信息
def personal_data(request):
    if 'username' in request.session:
        username = request.session['username']
        if username in User.username:
            return HttpResponse(JsonResponse({
                'data': list(User.objects.all())
            }))
        else:
            return JsonResponse({
                'userdata': '没有数据'
            })
    else:
        return JsonResponse({
            'userdata': '您还没有登录'
        })


# 文章详情页(纯文本)
def article_details(request, username, article_id):
    user = User.objects.filter(username=username)  # 记录用户
    article = PersonalArticle.objects.filter(article_id=article_id)  # 记录文章id
    articles = PersonalArticle.objects.all().values()
    record = BrowsingHistory.objects.create(user=user, articles=article)
    record.save()
    if articles:
        # data = list(articles)
        # print(data)
        return JsonResponse({
            'data': list(articles)
        })
    else:
        return JsonResponse({
            'messages': '没有文章请登录后发表'
        })


# 图片文章详情页
# def images_details(request):
#     images = Image.objects.all().values()
#     if images:
#         # images_data = list(images)
#         return JsonResponse({
#             'images_data': list(images)
#         })
#     else:
#         return JsonResponse({
#             'images': '您还没有图片，请登录后发表！'
#         })
#
#
# # 视频详情页
# def video_details(request):
#     videos = Video.objects.all()
#     if videos:
#         return JsonResponse({
#             'videos': videos
#         })
#     else:
#         return JsonResponse({
#             'messages': '还没有视频，请登录后上传'
#         })


# 浏览事迹
def browse_stories(request):
    articles = PersonalArticle.objects.all()
    if articles:
        return JsonResponse({
            'content': articles.order_by('read_count')[:10]
        })
    else:
        return JsonResponse({
            'error': '没有文章，请登录后发表'
        })


# 搜索文章
def search_article(request):
    title = request.GET.get('title', '')
    if title:
        articles = PersonalArticle.objects.filter(title__contains=title)
        return JsonResponse({
            'content': articles
        })
    else:
        return JsonResponse({
            'content': '没有文章，请登录后发表'
        })


# 评论
def comments(request):
    comment = Comment.objects.all().values()

    if comment:
        return JsonResponse({
            'comment': list(comment)
        })
    else:
        return JsonResponse({
            'comment': '暂时没有评论，请登录发表你的第一条评论吧！'
        })


# 分类查看
# def classification(request, category_type):
#     articles = PersonalArticle.objects.filter(category_type__exact=category_type).values()
#     # articles = PersonalArticle.objects.all()
#     data = list(articles)
#     if articles:
#         return JsonResponse(data, safe=False)
#     else:
#         return JsonResponse({
#             'message': '没有数据'
#         })
