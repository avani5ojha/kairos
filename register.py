import pymysql
import cgi

db=pymysql.connect("localhost", "root", "password", "stdb")
print("Content-Type:text/html") #ignores unnecessary Information
print("")

cursor=db.cursor()

data=cgi.FieldStorage() #extracts full html page ,taking data from apache and storing in web variable

sid=data.getvalue("sid")
sname=data.getvalue("sname")
address=data.getvalue("address")
email=data.getvalue("semail")
fname=data.getvalue("fname")
mname=data.getvalue("mname")

sql1="insert into student_detail values(%d,%s,%s,%s,%s,%s)"(sid, sname, address, email, fname, mname)
cursor.execute(sql1)
db.commit()
db.close()
