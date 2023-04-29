# bagian Muhammad Fandi Perdana 094
import mysql.connector

def create_connection():
        conn = None
        try:
            conn = mysql.connector.connect(
                host="db4free.net",
                user="fandiperdana",
                password="kelompok12",
                database="kelompok12"
            )
            print("Database connection successful!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        return conn
conn = create_connection()
# selesai Muhammad Fandi Perdana