import PyPDF2
import re
import smtplib
import mysql.connector
from email.message import EmailMessage
from attach3 import fileName,pick_mail

#parsing section
pdfob=open('/home/wst/Desktop/python-projects/download attachments/'+fileName,'rb')
pdfreader=PyPDF2.PdfReader(pdfob)
x=len(pdfreader.pages)
text=''
for i in range(0,x):
    pageobj=pdfreader.pages[i]
    text=text+pageobj.extract_text()
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
#print(emails)
Phonenumber=re.findall(r"[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+",text)
#print(Phonenumber)
skills='MYSQL|PHP|BOOTSTRAP|PLC|SCADA|HTML|html|CSS|css|Angular|Angularjs|PYTHON|python|JAVA|java|'
full_Skills=re.findall(skills, text, flags=re.IGNORECASE)
dub_full_Skills=[*set(full_Skills)]
upper_letter=[x.upper() for x in dub_full_Skills ]
dub1_full_Skills=[*set(upper_letter)]
listToStr1 = ' '.join([str(elem) for elem in emails])
listToStr2 = ' '.join([str(elem) for elem in Phonenumber])
listToStr3 = ' '.join([str(elem) for elem in dub1_full_Skills])


mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mydatabase')
mycursor=mydb.cursor()
sql1=mycursor.execute("SELECT * FROM resume")
result=mycursor.fetchall()[-1]
last_fetch=result[1]


if emails[0] == last_fetch:
    alert='this resume already parsing'
elif emails[0] != last_fetch:


 #Acknowledgement section
 msg=EmailMessage()
 msg['subject']='Thank You For Contacting us'
 msg['From']='samalin555@gmail.com'
 msg['To']=pick_mail

 msg.set_content('Hai is a Acknowledgement.we are received your Resumes.')

 server=smtplib.SMTP_SSL('smtp.gmail.com',465)
 server.login('samalin555@gmail.com','ygaomoyakiuczzdi')
 server.send_message(msg)
 server.quit
 #Acknowledgement section


 #database session
 mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mydatabase')
 mycursor=mydb.cursor()
 #mycursor.execute("CREATE TABLE resume (email VARCHAR(25), address VARCHAR(255))")
 #mycursor.execute("CREATE DATABASE mydatabase")
 sql = "INSERT INTO resume (mail_address, phone_num,skill) VALUES (%s, %s, %s)"
 val = (listToStr1, listToStr2,listToStr3)
 mycursor.execute(sql, val)
 mydb.commit()
 #print(mycursor.rowcount, "record inserted.")






    


        
    
   



