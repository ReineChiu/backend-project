from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

from . import models
from datetime import datetime

import json, boto3, re, base64
from django.conf import settings

from .models import Upload
from io import BytesIO

s3 = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
)

# Create your views here.
def message(request):
    return render(request, 'message.html')

def uploadFile(request):
    try:
        if request.method == "POST":
            image = request.FILES.get('image')
            text = request.POST.get('text')

            obj = Upload(content=text, file_name=image.name) 
            obj.save()

            s3.upload_fileobj(
                image,
                settings.AWS_STORAGE_BUCKET_NAME,
                settings.AWS_STORAGE_BUCKET_FOLDER + image.name
            )

            return JsonResponse({"ok":True, "message":"上傳檔案成功"})
        return JsonResponse({"error":True, "message":"上傳檔案不成功"})
    except Exception as e: 
        print(f"{e}:獲取上傳資料發生錯誤")
        return ({"error":True, "message":"獲取上傳資料過程發生錯誤"})

def getFile(request):
    try:
        if request.method == "GET":
            all_content = Upload.objects.all().values("content","file_name").order_by("-time")
            all_content = list(all_content)

            data = {"data":all_content}

            return JsonResponse({"ok":True, "data":data})
        return JsonResponse({"error":True, "message":"沒有取得檔案"})
    except Exception as e: 
        print(f"{e}:取得資料發生錯誤")
        return ({"error":True, "message":"取得資料過程發生錯誤"})

