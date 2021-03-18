from django.shortcuts import render, redirect

def index(req):
    
    counter = increment_counter(req)
    inc = int(req.session['inc']) if 'inc' in req.session else 1

    return render(req, "index.html", {"counter": counter, "inc": inc})

def reset(req):
    if 'counter' in req.session:
        del req.session['counter']
        req.session['inc'] =1;
        return redirect("/")
def increment(req, by=1 ):
    

    by  = int(req.POST['inc']) if 'inc' in req.POST else by

    counter = increment_counter(req, by)
    inc = req.session['inc']
    req.session['inc'] = by
    return render(req, "index.html", {"counter": counter, "inc": inc})

def increment_counter(req, by=1, start=0):
    x = int(req.session['counter']) if 'counter' in req.session else start

    counter = x + by
    req.session['counter'] = counter
    req.session['inc'] = by
    return counter

