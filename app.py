

from flask import Flask,render_template



app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/Tools")
def Tools():
    return render_template("Tools.html")

@app.route("/plan")
def plan():
    return render_template("plan.html")

@app.route("/Labs")
def Labs():
    return render_template("Labs.html")






if __name__=="__main__":
    app.run(debug=True)

