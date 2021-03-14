from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def index():

    return render_template("playground.html", count=3, color="#cccccc")


@app.route("/play/<int:count>")

def withCount(count): 
    return render_template("playground.html", count=count, color="#cccccc")

@app.route("/play/<int:count>/<color>")

def withCountAndColor(count, color): 
    return render_template("playground.html", count=count, color=color)

if __name__ =="__main__": 
    app.run(debug=True)