# MySQLServer.py

import mysql.connector

try:
    
    mydb = mysql.connector.connect(
        host="localhost", 
        user="root",       
        password="your_password" # Replace with your MySQL password
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Create the database if it doesn't exist
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")

    # Close the cursor and connection
    mycursor.close()
    mydb.close()

except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")
