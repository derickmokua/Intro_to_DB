🌟 Project Overview
Welcome to an exciting journey into the world of databases! This project introduces foundational concepts and practical skills for working with relational databases through the creation of a complete Online Bookstore Database System.
What You'll Build
A fully functional MySQL database for an online bookstore that manages:

📖 Books inventory
✍️ Author information
👥 Customer records
🛒 Orders and transactions
📦 Order details

🎯 Learning Objectives
By completing this project, you'll master:

✅ Understanding what databases and relational databases are
✅ SQL (Structured Query Language) fundamentals
✅ MySQL database management
✅ DDL (Data Definition Language) - CREATE, ALTER, DROP
✅ DML (Data Manipulation Language) - SELECT, INSERT, UPDATE, DELETE
✅ CRUD operations (Create, Read, Update, Delete)
✅ Database relationships using Foreign Keys
✅ Advanced SQL techniques including subqueries
✅ MySQL functions for data manipulation
✅ Python-MySQL integration

🗂️ Database Schema
alx_book_store Database Structure
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Authors   │         │    Books     │         │  Customers  │
├─────────────┤         ├──────────────┤         ├─────────────┤
│ author_id   │────────>│ book_id      │         │ customer_id │
│ author_name │         │ title        │         │ customer_name│
└─────────────┘         │ author_id    │         │ email       │
                        │ price        │         │ address     │
                        │ publication_ │         └─────────────┘
                        │ date         │                │
                        └──────────────┘                │
                               │                        │
                               │                        │
                               v                        v
                        ┌──────────────┐         ┌─────────────┐
                        │Order_Details │         │   Orders    │
                        ├──────────────┤         ├─────────────┤
                        │orderdetailid │         │ order_id    │
                        │ order_id     │<────────│ customer_id │
                        │ book_id      │         │ order_date  │
                        │ quantity     │         └─────────────┘
                        └──────────────┘
📋 Project Tasks
Task 0: Database Schema Design 🎨
File: alx_book_store.sql
Create the complete database schema with all tables and relationships.
Task 1: Database Creation with Python 🐍
File: MySQLServer.py
Write a Python script that automatically creates the database with proper error handling.
Features:

Creates alx_book_store database
Handles existing database gracefully
Includes connection error management
Prints success/failure messages

Task 2: Table Creation 🏗️
File: task_2.sql
SQL script to create all five tables: Authors, Books, Customers, Orders, and Order_Details.
Task 3: List All Tables 📝
File: task_3.sql
Query to display all tables in the database.
Task 4: Table Description 🔍
File: task_4.sql
Show the complete structure of the Books table.
Task 5: Single Data Insertion 📥
File: task_5.sql
Insert the first customer record into the database.
Task 6: Multiple Data Insertion 📦
File: task_6.sql
Batch insert multiple customer records efficiently.
🚀 Getting Started
Prerequisites

MySQL Server 5.7 or higher
Python 3.x
mysql-connector-python library

Installation

Clone the repository

bashgit clone https://github.com/yourusername/Intro_to_DB.git
cd Intro_to_DB

Install Python dependencies

bashpip install mysql-connector-python

Configure MySQL credentials

Edit MySQLServer.py and update:
pythonuser='your_mysql_username'
password='your_mysql_password'
Usage
Method 1: Using Python Script
bashpython MySQLServer.py
Method 2: Using SQL Files
bash# Create database and all tables
mysql -u root -p < alx_book_store.sql

# Or create tables separately
mysql -u root -p alx_book_store < task_2.sql

# List all tables
mysql -u root -p alx_book_store < task_3.sql

# Describe Books table
mysql -u root -p alx_book_store < task_4.sql

# Insert data
mysql -u root -p alx_book_store < task_5.sql
mysql -u root -p alx_book_store < task_6.sql
📁 Project Structure
Intro_to_DB/
│
├── alx_book_store.sql      # Complete database schema
├── MySQLServer.py          # Python database creation script
├── task_2.sql              # Create tables
├── task_3.sql              # List tables
├── task_4.sql              # Describe Books table
├── task_5.sql              # Insert single customer
├── task_6.sql              # Insert multiple customers
└── README.md               # Project documentation
🔑 Key Concepts
DDL vs DML
DDL (Data Definition Language)

CREATE - Create database objects
ALTER - Modify database objects
DROP - Delete database objects

DML (Data Manipulation Language)

SELECT - Retrieve data
INSERT - Add new data
UPDATE - Modify existing data
DELETE - Remove data

CRUD Operations

Create - INSERT new records
Read - SELECT data from tables
Update - UPDATE existing records
Delete - DELETE records

📚 Resources

What is Database & SQL?
Types of Databases (SQL & NoSQL)
MySQL Documentation
SQL Tutorial
Python MySQL Connector

🎓 Learning Path

✨ Start with understanding database concepts
🏗️ Learn to create databases and tables
📊 Master data insertion and retrieval
🔄 Practice CRUD operations
🚀 Explore advanced SQL techniques
🐍 Integrate Python with MySQL

🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
👨‍💻 Author
Derick Mokua

GitHub: derick_mokua

📝 License
This project is MIT licensed.
🎉 Acknowledgments

ALX Africa for the amazing curriculum
The MySQL community for excellent documentation
All contributors who helped improve this project

🌟 Show Your Support
Give a ⭐️ if this project helped you learn databases!

<div align="center">
  <strong>Happy Coding! 🚀</strong>
  <br>
  <em>Made with ❤️ for database beginners everywhere</em>
</div>
📊 Project Status
Show Image
Status: ✅ All tasks completed

🔥 Next Steps
After completing this project, you can:

Add more complex queries with JOINs
Implement stored procedures
Create database triggers
Build a web interface using Flask or Django
Learn about database optimization and indexing
Explore database normalization techniques

💡 Pro Tips

Always backup your database before major changes
Use consistent naming conventions
Document your SQL queries
Practice writing efficient queries
Learn to read MySQL error messages
Use transactions for data integrity
Keep your credentials secure
