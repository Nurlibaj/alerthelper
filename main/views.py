from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("hello")
def index(req):
    return render(req,'main/index.html')