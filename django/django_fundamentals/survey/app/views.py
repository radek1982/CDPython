from django.shortcuts import render,redirect

# Create your views here.

def index(req): 
    return render(req,"index.html")

def result(req):

    if req.method.upper() == "GET": return redirect("/")
    name = req.POST["name"]
    location = req.POST["location"]
    comment = req.POST["comment"]
    likesDjango = req.POST["likesDjango"]
    if len(name) == 0 or len(location) == 0: 
        return redirect("/")

    if len(comment) == 0: comment = "<None>"
    return render(req,"result.html", {
        "name": name, "location": location, "comment": comment, "likesDjango": likesDjango} )