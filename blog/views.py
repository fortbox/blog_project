# coding=utf-8
from django.shortcuts import render
import logging
from django.conf import settings
from models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

logger = logging.getLogger("blog.views")


# Create your views here.
def global_setting(request):
    return {
        'SITE_URL': settings.SITE_URL,
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }


def index(request):
    try:
        # 分类信息获取（导航数据）
        category_list = Category.objects.all()
        # 最新文章数据
        article_list = Article.objects.all()
        article_list = getPage(request, article_list)
        # 文章归类
        # 1，先要去获取到文章中有的 年份-月份
        archive_list = Article.objects.distinct_date()
        print("henry xiao" + str(archive_list))
    except Exception as e:
        logger.error(e)
    return render(request, "index.html", locals())


def archive(request):
    try:
        # 先获取客户端提交的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        print("henry xiao:year:" + str(year))
        print("henry xiao:month:" + str(month))
        # 最新文章数据
        article_list = Article.objects.filter(date_publish_icontains=year + '-' + month)
        print("henry xiao" + type(article_list))
    except Exception as e:
        logger.error(e)
    return render(request, "archive.html", locals())


# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 10)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


# 文章详情
def article(request):
    try:
        # 获取文章id
        id = request.GET.get('id', None)
        try:
            # 获取文章信息
            article = Article.objects.get(pk=id)
        except Article.DoesNotExist:
            return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    except Exception as e:
        print e
        logger.error(e)
    return render(request, 'article.html', locals())
