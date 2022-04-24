from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("歡迎使用")

def user_list(request):
    return HttpResponse("用戶列表")

def user_add(request):
    return HttpResponse("添加用戶")
