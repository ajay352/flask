from flask import Flask,render_template
from Respars import listToStr1 
import mysql.connector
app=Flask(__name__)

@app.route('/')
def home():
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mydatabase')
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM resume")
    myresult = mycursor.fetchall()
    
    return render_template('home.html',result=myresult,list1=listToStr1)

if(__name__=='__main__'):
    app.run(debug=True)    