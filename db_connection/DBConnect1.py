import mysql.connector
# open database connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
#password ad given in mysql

#prepare cursor object using cursor() method
cursor=db.cursor()

#execute sql query using execute
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone() method;

data=cursor.fetchone()
print("databse version:",data)

#disconnect from the server
db.close()
