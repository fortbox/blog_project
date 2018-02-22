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
        # 广告数据（同学们自己完成）
        # 最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list, 10)
        try:
            page = int(request.GET.get('page', 1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
        # 文章归类
        # 1，先要去获取到文章中有的 年份-月份
        archive_list = Article.objects.distinct_date()
        print("henry xiao" + str(archive_list))
    except Exception as e:
        logger.error(e)
    return render(request, "index.html", locals())
