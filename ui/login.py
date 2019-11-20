from flask import Flask,render_template, redirect, url_for, request, jsonify
import json
import time
import mysql.connector
from BSTuser import bst, Node

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="a8888888",
  database="PCA"
)

mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('loginPage.html')  

@app.route('/register')
def RegisterPage():
    return render_template('Regis.html')

@app.route('/login', methods=['POST'])
def Enroll():
    if request.method == "POST":
        User = request.form['user']
        Pw   = request.form['psw']
        
        mycursor.execute("INSERT INTO PROJECT (Name,Time ) VALUES (%s,%s);",(User,Pw))
        mydb.commit()
        
        mycursor.execute("SELECT * FROM PROJECT")
        myresult = mycursor.fetchall()
        for x in myresult:
            bst.insert(Node(x[1],x[2]))
        print(bst.count(bst.root))

        return render_template('loginPage.html') 

@app.route('/loginsuccess')
def Success():
    return render_template('successful.html')



    



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8000)