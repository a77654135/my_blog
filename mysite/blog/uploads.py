# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
import json
import datetime
import uuid
import os

import logging

logger = logging.getLogger()

@csrf_exempt
def upload_images(request, dir_name):
    result = {"error": 1, "message": u"上传出错"}

    img_file = request.FILES.get("imgFile", None)
    if img_file:
        result = upload_image(dir_name, img_file)
    return HttpResponse(json.dumps(result), content_type='application/json')


def upload_image(dir_name, img_file):
    file_name = img_file.name
    allow_suffix = ["png", "jpg", "gif", "jpeg", "bmp"]
    suffix = file_name.split(".")[-1]
    if suffix not in allow_suffix:
        return {"error": 1, "message": u"图片格式不正确"}

    dir_name = get_relative_dir(dir_name)
    dir_path = os.path.join(settings.MEDIA_ROOT, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_name = "{}.{}".format(str(uuid.uuid1()), suffix)
    file_path = os.path.join(dir_path, file_name)
    file_url = "{}/{}/{}".format(settings.MEDIA_URL, dir_name, file_name)
    with open(file_path, "wb") as f:
        f.write((img_file.file.read()))
    return {"error": 0, "url": file_url}


def get_relative_dir(dir_name):
    today = datetime.datetime.today()
    name = "{}/{}/{}".format(dir_name, today.year, today.month)
    return name
