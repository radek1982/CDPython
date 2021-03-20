from django.shortcuts import render, redirect
from .models import User

def index(req):

   

        

    users = User.objects.all()

    return render(req,"index.html", {"users": users})

def create(req):
     if  'add' in req.POST:
        first  = req.POST.get('first')
        last  = req.POST.get('last')
        email = req.POST.email('email')
        age  = req.POST.get('age')

        User.objects.create(first_name= first, 
        last_name=last, email="email", age =age )
        
        return redirect("/")
    