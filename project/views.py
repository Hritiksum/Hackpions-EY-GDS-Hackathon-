#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage

#his=[]
#from .models import *



def upload_OD(request):
    import requests
    import glob
    import os
    import pytesseract
    import shutil
    import os
    import random
    try:
        from PIL import Image
    except ImportError:
        import Image
        import cv2
        import pytesseract
    text=''
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)

        list_of_files = glob.glob('media/*.png') # * means all if need specific format then *.png
        latest_file = max(list_of_files, key=os.path.getctime)
        print (str(latest_file))

        pytesseract.pytesseract.tesseract_cmd = (r'/usr/bin/tesseract')
        text = pytesseract.image_to_string(Image.open(latest_file))
            
    return render(request,'upload_OD.html',{'result':text,'f5':"Copy paste the image OR upload"})


def error_404_view(request, exception):
    return render(request,'404.html')

def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, '404.html')