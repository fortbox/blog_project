# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     upload.py
   Description :
   Author :       jacky
   date:          2/13/2018
-------------------------------------------------
   Change Activity:
                   2/13/2018:
-------------------------------------------------
"""
__author__ = 'jacky'
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import os
import uuid
import json
import datetime as dt
import logging

logger = logging.getLogger("blog.upload")

##################
#  kindeditor图片上传返回数据格式说明：
# {"error": 1, "message": "出错信息"}
# {"error": 0, "url": "图片地址"}
##################
@csrf_exempt
def upload_image(request, dir_name):
    """
    :param request:
    :param dir_name:
    :return:
    """
    result = {"error": 1, "message": "上传出错"}
    files = request.FILES.get("imgFile", None)
    logger.error(files)
    logger.error(type(files))
    if files:
        result = image_upload(files, dir_name)
    return HttpResponse(json.dumps(result),
                        content_type="application/json")


# 目录创建
def upload_generation_dir(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name + '/%d/%d/%d/' % (today.year, today.month, today.day)
    if not os.path.exists(settings.MEDIA_ROOT + dir_name):
        os.makedirs(settings.MEDIA_ROOT + dir_name)
    logger.error(dir_name)

    return dir_name


# 图片上传
def image_upload(files, dir_name):
    # 允许上传的文件类型
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        return {"error": 1, "message": "图片格式不正确"}
    relative_path_file = upload_generation_dir(dir_name)
    path = os.path.join(settings.MEDIA_ROOT, relative_path_file)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = str(uuid.uuid1()) + "." + file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL + relative_path_file + file_name
    open(path_file, 'wb').write(files.file.read())
    return {"error": 0, "url": file_url}
