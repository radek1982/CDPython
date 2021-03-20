from django.shortcuts import render,redirect
from random import randint
from time import gmtime,strftime

farm = {"id": 1, "location": "Farm", "description": "(Earns 10-20 Gold)", "min": 10, "max":20}
cave = {"id": 2, "location": "Cave", "description": "(Earns 5-10 Gold)", "min": 5, "max":10}
house = {"id": 3, "location": "House", "description": "(Earns 2-5 Gold)", "min": 2, "max":5}
casino = {"id": 4, "location": "Casino", "description": "(Earns/Looses 0-50 Gold)", "min": -50, "max":50}

quests = [farm,cave,house,casino]
def index(req):
    return render(req, "index.html", {"gold":adjust_gold(req), "quests": quests, "log": log(req)})

def process_money(req): 
  
   quest_id= int(req.POST.get('quest_id',0))
   q =  quests[quest_id -1 ]
   gold = randint(q["min"], q["max"])
   adjust_gold(req, gold)
   outcome = "good" if gold > 0 else "bad"
   location = q["location"].lower()

   log_msg(req, outcome, gold, location)
  
   return redirect("/")

def log_msg(req,outcome, gold, location):
 
   l= log(req)


   time  = strftime("%m/%d/%Y, %H:%M:%S %p", gmtime())
   msg = f"Earned {currency(abs(gold))} from {location}!" if outcome  == "good" else f"Entered a {location} and lost {currency(abs(gold))} gold!"

   m = {"outcome": outcome, "location": location, "msg": msg, "time": time}
 
   l.append(m)
   req.session['log'] = l

   return log
def log(req):
  return req.session['log'] if 'log' in req.session else []

def adjust_gold(req, amount = 0):
  gold =  float(req.session['gold']) + amount if 'gold' in req.session else 0.0
  req.session['gold'] = gold
  return currency(gold)

def reset(req):
    if 'log' in req.session: del req.session['log']
    if 'gold' in req.session: del req.session['gold']

    return redirect("/")

def currency(amount):
  return f"${amount:.2f}"

def abs(amount): 
    return amount*-1 if amount<0 else amount




  