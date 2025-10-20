#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database if it doesn't exist."""
    connection = None
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password=''   # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # CREATE DATABASE statement for alx_book_store
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            print("Database 'alx_book_store' created successfully!")
            
            cursor.close()
    
    # Handle exceptions
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
