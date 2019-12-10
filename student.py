from flask import *
from flask_mail import Mail, Message
import random as r
import pymysql as sql
def addToDatabase(userID,name,dob,fname,pwd,sex,idType,uidno,phone,email):
    conn=sql.connect(host="localhost",user="root",password="",database="major")
    if(conn):
        cursor=conn.cursor()
        insertQuery="INSERT INTO regis(userID,name,dob,fname,pwd,sex,idtype,uidno,phone,email) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        x=(userID,name,dob,fname,pwd,sex,idType,uidno,phone,email)
        cursor.execute(insertQuery,x)
        conn.commit()
        return True
    else:
        print("ERROR! Couldn't register!")
        return False
def generateUserID(dob):
    dobArray=dob.split("-")
    x=r.randint(1001,10001)
    res="2020"
    for i in dobArray:
        res=res+i
    res=res+str(x)
    return res
app=Flask(__name__)
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'khanarpit528@gmail.com'
app.config['MAIL_PASSWORD'] = 'tanmoydoescss'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)
@app.route("/student")
def stu():
    return render_template('stu.html')
@app.route("/student/registration")
def student_reg():
    return render_template('student_reg.html')
@app.route("/student/login")
def student_login():
    return render_template('student_login.html')
@app.route("/student/s_register",methods=['GET','POST'])
def parseForm():
    if(request.method=="POST"):
        dob=request.form["dob"]
        userID=generateUserID(dob)
        name=request.form["name"]
        fname=request.form["fname"]
        pwd=request.form["pwd"]
        sex=request.form["gender"]
        idType=request.form["govtid"]
        uidno=request.form["uidno"]
        phone=request.form["phone"]
        email=request.form["email"]
        status=addToDatabase(userID,name,dob,fname,pwd,sex,idType,uidno,phone,email)
        if(status):
            res=sendMail(userID,name,email)
        else:
            print("SQL operation failed!")
    return render_template('s_register.html')
def sendMail(userID,name,email):
    msg=Message("Registration confirmation",sender="khanarpit528@gmail.com",recipients=[email])
    msg.body="Hello %s. Your registration was successful! Your user ID is %s" % (name,userID)
    mail.send(msg)
    return "Sent"
if __name__ == '__main__':
    app.run(debug=True)
