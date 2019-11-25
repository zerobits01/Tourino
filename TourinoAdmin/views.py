from django.shortcuts import render
from django.http import request,JsonResponse
# Create your views here.

def home():
    return JsonResponse({
        'msg' : 'home page'
    },status=200)