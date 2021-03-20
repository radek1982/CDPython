from django.shortcuts import render, redirect
from .models import *

def index(req): 



    data =  [{"id": d.id,"name": d.name, "count": "No" if d.ninjas.count() == 0 else d.ninjas.count, "ninjas": [f"{n.first_name} {n.last_name} " for n in d.ninjas.all()]} 
        for d in Dojo.objects.all()]

    dojo_dropdown  = [{"id": d.id, "name": d.name} for d in Dojo.objects.all()]
        
    return render(req, "index.html", {"data": data, "dojo_dropdown": dojo_dropdown})

def add_dojo(req):
    if req.POST['add_dojo']:
        name = req.POST['name']
        city = req.POST['city']
        state = req.POST['state']
    
    Dojo.objects.create(name = name, city = city, state = state)
    return redirect("/")

def add_ninja(req): 
      if req.POST['add_ninja']:
        first = req.POST.get("first_name", "")        
        last = req.POST.get('last_name', "")
        dojo = req.POST.get('dojo', 0)
        
        d = Dojo.objects.get(id=dojo)
    
        Ninja.objects.create( first_name = first, last_name = last , dojo = d)
        return redirect("/")

def delete_dojo(req, dojo_id):
        Dojo.objects.get(id=dojo_id).delete()
        return redirect("/")