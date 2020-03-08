import json, time, cv2
import flask
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, jsonify
import shutil, os
app = Flask(__name__)
from eval import main

#Basic Web Pages
#-------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/test/<msg>")
def test(msg):
    return "Hello"+str(msg)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

#Main Web Pages
#-------------------------------------------------------------------------------------------
@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/demo_crop")
def demo_crop():
    return render_template("demo_crop.html")

@app.route("/demo_result")
def demo_result():
    return render_template("demo_result.html")

# Web Upload Functions
#-------------------------------------------------------------------------------------------
@app.route("/invoice_upload", methods=["POST"])
def invoice_upload():
    if request.method == "POST":
        f= request.files["image"]
        uid = request.form["uid"]
        id = int(time.time())
        basedir = os.path.abspath(os.path.dirname(__file__))
        f.save(os.path.join(basedir, "static/uploads/", str(uid)+"/"+str(id)+".png"))
        return render_template("crop.html", image_name=id)
'''

@app.route("/invoice_upload", methods=["POST"])
def invoice_upload():
    if request.method == "POST":
        f= request.files["image"]
        id = int(time.time())
        basedir = os.path.abspath(os.path.dirname(__file__))
        f.save(os.path.join(basedir, "static/uploads", str(id)+".png"))
        return render_template("crop.html", image_name=id)

@app.route("/crop/<id>/<x1>/<y1>/<x2>/<y2>")
def crop(id,x1,y1,x2,y2):
    print(id,x1,y1,x2,y2)
    img = cv2.imread("./static/uploads/{}.png".format(id))
    img_crop = img[int(y1):int(y2), int(x1):int(x2)]
    cv2.imwrite("./static/uploads/{}.png".format(id), img_crop)
    #json = main("./static/uploads/{}.png".format(id))
    # return redirect(url_for("/show",image_name=id))
    return redirect(url_for("result",image_name=id))
'''

@app.route("/crop", methods=["POST"])
def crop():
    id, x1,y1,x2,y2 = int(request.form["id"]),int(request.form["x1"]),int(request.form["y1"]),int(request.form["x2"]),int(request.form["y2"])
    print(id, x1,y1,x2,y2)
    img = cv2.imread("./static/uploads/{}.png".format(id))
    yo, xo, ch = img.shape
    scale = yo/650
    y1_new = scale*y1
    x1_new = scale*x1
    y2_new = scale*y2
    x2_new = scale*x2
    img_crop = img[int(y1_new):int(y2_new), int(x1_new):int(x2_new)]
    cv2.imwrite("./static/uploads/{}.png".format(id), img_crop)
    return "Hello World"
    return redirect(url_for("result",image_name=id))

@app.route("/result/<image_name>")
def result(image_name):
    json = main("./static/uploads/{}.png".format(id))
    # json = {"vendor":"mohan", "date":'23/5/2019', "amount":"45","items":"colagte, pepsodent"}
    # print(jsonify(json))
    # print(json)
    return render_template("result.html",image_name=image_name, json = json)
    # return render_template("result.html",image_name=image_name, json="{'company':'abc'}")

# Android Specific Functions
#-------------------------------------------------------------------------------------------
@app.route("/random", methods=['GET', "POST"])
def random():
    #print(request.data)
    url = request.data.decode('UTF-8')
    #print("URL printing: ",url)
    os.system("wget \"{}\" -O temp.jpg".format(url))
    useful = url.split("/o/")[1]
    uid,transid = useful.split("%2F")[0:2]
    #transid = useful.split("%2F")[1]
    main("temp.jpg", uid+"_"+transid)
    return "Job done!"

# https://firebasestorage.googleapis.com/v0/b/expense-tracker-7e30c.appspot.com/o/Dt014Ow9GaPbZKwuOND7F6dCcxw1%2F1812%2Fstorage%2F2166-1715%2FDCIM%2FCamera%2FIMG_20200221_133437_HDR.jpg?alt=media&token=9e3346e4-8908-4afc-9f0d-e8646559c0ce

#app.run(host="0.0.0.0", port="5000", debug=False)
#python -m flask run --host 0.0.0.0 --port 5000
