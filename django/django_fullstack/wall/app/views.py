from django.http import HttpRequest
from django.shortcuts import render,redirect
from app.models import *

# Create your views here.

def index(req: HttpRequest):
    user = _current_user(req)   
    return render(req, "index.html", {"user": user, "messages": Message.objects.all().order_by("-created_at")})



def reset(req):

    Message.objects.all().delete()

    return redirect("/")

def _current_user(req:HttpRequest):

    user = None 
    if req.session.get("current_user"):
         id = int(req.session.get("current_user"))
         user = User.objects.get(id=id)
    return user

def post(req: HttpRequest):
    user = _current_user(req)

    if user == None:
        user = User.objects.first()
        _login(req, user)

    text = req.POST.get("text", "this is a sample")

    if user: 
        user.messages.create(message =text)

    return redirect("/")

def comment(req: HttpRequest, msgid:int):
    user = _current_user(req)

    if user == None:
        user = User.objects.first()
        _login(req, user)

    msg = Message.objects.get(id=msgid)
    text = req.POST.get("text", "Sample Comment")

    msg.comments.create( message=msg, comment =text, user=user)

    return redirect("/")

def _login(req:HttpRequest, user: User):
    
        req.session["current_user"] = user.id
        req.session.save()