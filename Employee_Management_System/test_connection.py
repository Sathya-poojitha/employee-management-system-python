import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sathyapoojisu@123"
)

if conn.is_connected():
    print("MySQL Connected Successfully")
