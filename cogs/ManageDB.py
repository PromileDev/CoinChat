import os 
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)

if conn.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")


cursor = conn.cursor()

cursor.close()
conn.close()