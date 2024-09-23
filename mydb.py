import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123"
)
#create a cursor object
cursorObject = database.cursor()
#create a database
cursorObject.execute("CREATE DATABASE mysql_db")

print("Database created")