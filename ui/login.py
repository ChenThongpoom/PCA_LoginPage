from flask import Flask,render_template, redirect, url_for, request, jsonify
import json
import time
# from tableQueue import Queue
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="a8888888",
#   database="PCA"
# )

# mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('loginPage.html')  

@app.route('/register')
def RegisterPage():
    return render_template('Regis.html')



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=8000)