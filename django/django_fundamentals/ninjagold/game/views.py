from django.shortcuts import render
from random import randint
from time import gmtime,strftime

farm = {"id": 1, "location": "Farm", "description": "(Earns 10-20 Gold)", "min": 10, "max":20}
cave = {"id": 2, "location": "Cave", "description": "(Earns 5-10 Gold)", "min": 5, "max":10}
house = {"id": 3, "location": "House", "description": "(Earns 2-5 Gold)", "min": 2, "max":5}
casino = {"id": 4, "location": "Casino", "description": "(Earns/Looses 0-50 Gold)", "min": -50, "max":50}

quests = [farm,cave,house,casino]
def index(req):
    log = req.session['log'] if 'log' in req.session else []
    return render(req, "index.html", {"quest_list": quest_list(), "log": log})

def quest_list(): 

    rendered = []
    for q in quests:
      loc = q['location']
      id = q['id']
      link = f"/take/{id}"
      rendered.append(f"<li class='quest'><div class='details'> <h2>{loc}</h2> <p> {q['description']} <a href='{link}'>Find gold! </a> </p> </div></li>")
    return "\n".join(rendered)
def take(req, quest_id): 
   q =  quests[quest_id]
   gold = randint(q["min"], q["max"])
   time  = strftime("%Y/%m/%d %h:%i:%s %p", gmtime())
   outcome = "good" if gold > 0 else "bad"
   location = q["location"].lower()

   log = req.session['log'] if 'log' in reg.session else []
   msg = f"<p class='good'>Earned {gold} from {location}! ({time}) </p>" if outcome  == "good" else f"<p class='bad'> Entered a {location} and lost {gold} gold. </p>"

   log.append(msg)
   req.session['log'] = log

   return render(req, "index.html", {"quests": quests, "log": log})