from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/dojo")
def dojo(): 
    return "Dojo!"

@app.route("/hi/<user>")
def hi(user): 
    return "Hi %s" % escape(user)

@app.route("/repeat/<int:times>/<word>")

def repeat(times, word):

    return "%s <br>" % escape(word) * times

@app.route("/<path:path>")
def catch_all(path):
    return "Sorry! no response. try again"

if __name__=="__main__":
    app.run(debug= True)