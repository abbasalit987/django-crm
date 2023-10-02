import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Gtr@vels123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE xyz")

print("All Done!")
