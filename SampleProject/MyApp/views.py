from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import io
import json
import subprocess
import io
# Create your views here.
#@api_view(['GET','POST'])

def get(request, cmd_id):
    if cmd_id == "ls":
        sut = subprocess.Popen("dir", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        with open(r"file1.txt","w") as file1:
            for line in io.TextIOWrapper(sut.stdout, encoding="utf-8"):
                file1.write(line)
            file1.close()
        file2 = open("file1.txt", "r")
        a=file2.read()
        dict1 = {
            "Output of ls" : a
        }
        return JsonResponse(dict1,safe=False)
    #return HttpResponse(a)
    elif cmd_id == "cwd":
        sut = subprocess.Popen("cd", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        with open(r"file1.txt","w") as file1:
            for line in io.TextIOWrapper(sut.stdout, encoding="utf-8"):
                file1.write(line)
            file1.close()
        file2 = open("file1.txt", "r")
        a=file2.read()
        dict1 = {
            "Output of cwd" : a
        }
        return JsonResponse(dict1,safe=False)
    #return HttpResponse(a)
    else:
        return HttpResponse("Only serve cwd commands here")

def aiacademy(requests):
    return render(requests, 'MyApp/first_figure.html')