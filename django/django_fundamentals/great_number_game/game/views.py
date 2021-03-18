from django.shortcuts import render
from random import randint
# Create your views here.

def index(req):
    secret =  get_secret(req,True);
    print(str(secret))

    req.session['guess_count'] = 1
    guess_count = 1

    return render(req,"index.html", {"secret": secret,  "guess_count": guess_count})

def guess(req):
    
    if req.POST != None:
        guess =  int(req.POST['guess'])      

    secret = get_secret(req)

    if guess < secret : return update_ui(req, "low")
    if guess > secret : return update_ui(req, "high")
    if guess == secret :return update_ui(req,"won")

def get_secret(req,generate = False):

    if generate: 
        req.session['secret']= randint(1,100)
    return req.session['secret']

def update_ui(req,result):
    if req.POST != None:
        guess =  int(req.POST['guess'])      

    secret = get_secret(req)


    if result!="won": 
      guess_count = mark_guess(req, True)
    else:
        guess_count=mark_guess(req)

    return render(req,"index.html", {"secret": secret, "guess": guess, "result": result, "guess_count": guess_count})

def mark_guess(req, increase = False):

    guess_count = req.session['guess_count'] if 'guess_count' in req.session else 0

    if increase:
        guess_count+=1
        req.session['guess_count'] = guess_count
    return guess_count

    