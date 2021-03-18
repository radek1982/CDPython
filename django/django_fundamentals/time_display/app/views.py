from django.shortcuts import render
from time import gmtime,strftime

# Create your views here.

def index(req):
    ctx = {
         "time": strftime("%b, %d %H:%M %p", gmtime())
    }
    return render(req, "index.html", ctx)