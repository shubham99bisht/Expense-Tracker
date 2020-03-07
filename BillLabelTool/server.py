import flask
from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os, json
app = Flask(__name__)

max_data = len(os.listdir("data"))-1

@app.route("/index/<id>")
def index(id):
    global max_data
    if int(id)>max_data: return "done"
    file = "data/"+str(id)+".txt"
    with open(file,"r") as f:
        text = f.read()
    return render_template("index.html", id=id, text=text)


@app.route("/submit", methods=["POST"])
def submit():
    global max_data
    oldid = int(request.form["id"])
    total = int(request.form["total_item"])
    result = request.form.to_dict(flat=False)

    json.dump(result, open("results/{}.json".format(oldid),"w"))

    newid = oldid+1
    if newid>max_data: return "done"
    else: return redirect("index/{}".format(newid))


@app.route("/guidelines")
def guidelines():
    return render_template("guidelines.html")
