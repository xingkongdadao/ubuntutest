from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloworld(req):
    return HttpResponse("Big Rollers")

def index(request):

    return render(request, 'index.html',locals())
