from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(' I changed this line....hello world')


def land(request):
    return render(request,'myland.html')
