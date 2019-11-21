from flask import Flask,render_template, redirect, url_for, request, jsonify
import json
import time
import mysql.connector
from BSTuser import BST, Node

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="a8888888",
  database="PCA"
)

mycursor = mydb.cursor()

app = Flask(__name__)
bst = BST()


@app.route('/')
def Home():
    global bst

    mycursor.execute("SELECT * FROM LOGIN")
    my = mycursor.fetchall()
    for x in my:
        bst.insert(Node(x[1],x[2]))
    return render_template('loginPage.html')  

@app.route('/register')
def RegisterPage():
    return render_template('Regis.html')

@app.route('/login', methods=['POST'])
def Enroll():
    global bst
    if request.method == "POST":
        User = request.form['user']
        Pw   = request.form['psw']
        if User not in (bst.preorder(bst.root)):
        
            mycursor.execute("INSERT INTO LOGIN (Name,Password ) VALUES (%s,%s);",(User,Pw))
            mydb.commit()

            return render_template('registerComplete.html') 
        else:
            return render_template('invalid.html')

@app.route('/loginsuccess',methods=['GET','POST'])
def Success():
    global bst
    if request.method == "POST":
        loginUser = request.form['uname']
        loginPw   = request.form['pwd']
        print(loginPw)
        print(bst.find(loginUser))
        if (str(bst.find(loginUser))) == loginPw:
            return render_template('successful.html')
        else:
            return render_template('unsuccessful.html')

@app.route('/forgot',methods=['GET','POST'])
def Forget():
    if request.method =="POST":
        forgotUser = request.form['fname']
        print(bst.find(forgotUser))
    return render_template('forgot.html')

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8000)