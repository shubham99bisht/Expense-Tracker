import json, time, cv2
import flask
from flask import Flask, render_template, request, send_from_directory, redirect, url_for, jsonify
import shutil, os
app = Flask(__name__)
from eval import main
import pytesseract

# https://pypi.org/project/python-firebase/
from firebase import firebase
firebase = firebase.FirebaseApplication('https://expense-tracker-7e30c.firebaseio.com/', None)


#Basic Web Pages
#-------------------------------------------------------------------------------------------
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/demo_crop")
def demo_crop():
    return render_template("demo_crop.html")

@app.route("/demo_result")
def demo_result():
    return render_template("demo_result.html")

#Main Web Pages
#-------------------------------------------------------------------------------------------
@app.route("/transaction")
def transaction():
    return render_template("transaction.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")

# Web Upload Functions
#-------------------------------------------------------------------------------------------
@app.route("/upload_and_crop", methods=["POST"])
def upload_and_crop():
    if request.method == "POST":
        f = request.files["image"]
        uid = request.form.get("uid")
        billid = request.form.get("billid")
        image_name = uid+"_"+billid
        basedir = os.path.abspath(os.path.dirname(__file__))
        f.save(os.path.join(basedir, "static/uploads/", image_name + ".png"))

        option = request.form.get("option")
        option = int(option.split(".")[0])

        # print(request.form.get("checkbox"))

        if option == 1:
            return render_template("crop.html", image_name=image_name)
        if option == 2:
            json = main(os.path.join(basedir, "static/uploads/", image_name+".png"))
            print(json, type(json))
            return render_template("result.html",image_name=image_name, json=json, uid=image_name.split("_")[0], billid=image_name.split("_")[1])
            # return render_template("result.html",image_name=image_name, json=json)

@app.route("/crop_and_result", methods=["POST"])
def crop_and_result():
    id, x1,y1,x2,y2 = request.form["id"],int(request.form["x1"]),int(request.form["y1"]),int(request.form["x2"]),int(request.form["y2"])
    print(id, x1,y1,x2,y2)
    img = cv2.imread("./static/uploads/{}.png".format(id))
    yo, xo, ch = img.shape
    scale = yo/650
    y1_new = scale*y1
    x1_new = scale*x1
    y2_new = scale*y2
    x2_new = scale*x2
    img_crop = img[int(y1_new):int(y2_new), int(x1_new):int(x2_new)]
    cv2.imwrite("./static/uploads/{}_crop.png".format(id), img_crop)
    time.sleep(1)

    basedir = os.path.abspath(os.path.dirname(__file__))
    json = main(os.path.join(basedir, "static/uploads/", id+"_crop.png"))
    return render_template("result.html",image_name=id+"_crop", json=json, uid=id.split("_")[0], billid=id.split("_")[1])

# Result Verification Page
#-------------------------------------------------------------------------------------------
@app.route("/result_verification/<billid>")
def result_verification(billid):
    billid = int(billid)
    return render_template("result_verification.html",billid=billid)

# Android Specific Functions
#-------------------------------------------------------------------------------------------
@app.route("/random", methods=['GET', "POST"])
def random():
    url = request.data.decode('UTF-8')
    # print("URL printing: ",url)

    useful = url.split("/o/")[1]
    uid,transid = useful.split("%2F")[0:2]
    print(uid, transid)
    name = uid+"_"+transid+".png"
    '''
    os.system("wget \"{}\" -O static/uploads/{}".format(url, name))
    json = main(name)
    json["Link"] = url
    json["Status"] = 0
    json["Category"] = "Misc"
    '''
    json = {
      "Address" : "Ground Floor, Shop no. 12 13 20 21& 22",
      "Amount" : "99.76",
      "Category" : "Food",
      "Company" : "TAX INVOCE",
      "Date" : "2/26/2020",
      "Items" : "1 Reg HT PM Paneer",
      "Link" : "https://firebasestorage.googleapis.com/v0/b/expense-tracker-7e30c.appspot.com/o/UUNs2qVregW6zrFJDQd7OEaKNV72%2F17%2FJPEG_20200331_182936.jpg?alt=media&token=ffabed8d-e1fd-43cf-b39f-5a07f1b86f8e",
      "Status" : "0"
    }
    print(json)
    result = firebase.put('/Bills/{}/'.format(uid), transid, json)
    return "Job done!"

# https://firebasestorage.googleapis.com/v0/b/expense-tracker-7e30c.appspot.com/o/Dt014Ow9GaPbZKwuOND7F6dCcxw1%2F1812%2Fstorage%2F2166-1715%2FDCIM%2FCamera%2FIMG_20200221_133437_HDR.jpg?alt=media&token=9e3346e4-8908-4afc-9f0d-e8646559c0ce
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

# host="0.0.0.0", port="5000", debug=False
#python -m flask run --host 0.0.0.0 --port 5000
