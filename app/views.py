from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def jalireddy(request):
    return HttpResponse('<h1><marquee>Jalireddy: I want load </h1></marquee>')

def pushpa(request):
    return HttpResponse('<h1><marquee> pushpa: ok....  </h1></marquee> ')