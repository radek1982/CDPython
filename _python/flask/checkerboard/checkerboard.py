from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():

    return render_template("checkerboard.html", cols=8, rows=8,light="#fff",dark="#999")
@app.route("/<int:rows>")
def rows(rows):
    return render_template("checkerboard.html", cols=8, rows=rows, light="#fff",dark="#999")

@app.route("/<int:rows>/<int:cols>")
def cols(rows,cols):
    return render_template("checkerboard.html", cols=cols, rows=rows, light="#fff",dark="#999" )


@app.route("/<int:rows>/<int:cols>/<light>/<dark>")
def colors(rows,cols, light, dark):
    return render_template("checkerboard.html", cols=cols, rows=rows, light=light, dark=dark)

if __name__ =="__main__": 
    app.run(debug=True)