#!/usr/bin/python3
"""
A script that creates the database alx_book_store in a MySQL server.
"""

import mysql.connector
from mysql.connector import errorcode

# Database connection parameters - replace with your actual credentials
# It's recommended to use environment variables or a config file for sensitive data.
DB_CONFIG = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
}
DB_NAME = 'alx_book_store'

def create_database():
    """Connects to MySQL server and creates the alx_book_store database."""
    cnx = None
    try:
        # Establish the connection
        cnx = mysql.connector.connect(**DB_CONFIG)
        cursor = cnx.cursor()

        # SQL statement to create the database
        # Using IF NOT EXISTS prevents an error if the database already exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
        print(f"Database '{DB_NAME}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Failed to create database: {err}")
    finally:
        # Close the connection
        if cnx and cnx.is_connected():
            cursor.close()
            cnx.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
