import mysql.connector

mydb - mysql.connector(
    host=:"localhost"
    user="jgutierrez"
    password="temppassword"
)

mycursor = mydb.cursor()

mycursor.execute ()