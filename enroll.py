import main.enroll
import pymysql

kf.settings.app_id=""
kf.settings.app_key=""

db=pymysql.connect("localhost", "root", "avani@mysql", "test")
cursor=db.cursor()

# sql2="select sid from test1 order by sid desc limit 1;"
sql2="SELECT MAX(sid) FROM test1;"
cursor.execute(sql2)
result=cursor.fetchone()


db.close()

# kf.enroll_face(file='face.jpg', subject_id=result[0] , gallery_name="student")
enroll('face.jpg' , result[0] , "student")
