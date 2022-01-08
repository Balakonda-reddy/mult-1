
from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST']='rdsdb.cjs0dwnk6jsz.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='vicky123'
app.config['MYSQL_DB']='balu'
mysql=MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/Registration',methods = ['GET','POST'])
def Registration():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password =request.form['password']
        Details = request.form['Details']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users (name,email,password,Details) VALUES(%s,%s,%s,%s)",(name,email,password,Details))
        mysql.connection.commit()
        cur.close()
        return redirect('/plan')
    return render_template("Registration.html")

@app.route("/plan")
def users():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * FROM users")
    if result>0:
        userDetails=cur.fetchall()
        return render_template("plan.html",userDetails=userDetails)

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
    app.run(debug=True,host='0.0.0.0',port=500)


