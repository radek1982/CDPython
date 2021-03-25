from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from app.models import User
from django.contrib import messages


SESSION_VAR_NAME="current_user_id"
def index(req:HttpRequest):


    return render(req, "index.html", {"data": req.POST})
def login(req:HttpRequest):

    email = req.POST.get("email") 
    password = req.POST.get(['password'])
    print(email, password)
    if email and password:
        u = User.login(email,password)


        if u:
            req.session[SESSION_VAR_NAME] = u.id
            req.session.save()
            return redirect("/success")
    messages.add_message(req, messages.WARNING, "Invalid login credentials")
    return redirect("/",)    
def logout(req):
    return _logout(req)
def register(req:HttpRequest):
    email = req.POST['email']
    passwd = req.POST['password']
    first = req.POST['first_name']
    last = req.POST['last_name']

    errors  = User.objects.validate_registration(req.POST)
    if (len(errors) == 0):
    
        x = User.objects.create(email  = email, first_name = first, last_name = last, password = passwd)
        req.session[SESSION_VAR_NAME] = x.id
        req.session.save()

        if x: 
            return redirect("/success")
    else:
        
        for m in errors:
     
            messages.add_message(req, messages.WARNING, f"Errors: {m}")
        return render(req, "index.html", {"data": req.POST})
def success(req):
       user = _current_user(req)
       messages.add_message(req, messages.INFO, f"Hello {user.first_name} <a href='/logout'>Log Out</a>")
       return render(req, "success.html", {"user": user})


def _current_user(req: HttpRequest):
    if SESSION_VAR_NAME in req.session:
        u = User.objects.get(id=req.session.get(SESSION_VAR_NAME))

        if u:
            return u
    else: 
        return redirect("/login")
def _logout(req:HttpRequest):
      if SESSION_VAR_NAME in req.session:
        del req.session[SESSION_VAR_NAME]
      messages.add_message(req, messages.INFO, f"You've been logged out")
      return redirect("/")
