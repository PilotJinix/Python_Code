import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Wxpy"
)

database = mydb.cursor()
database.execute("CREATE TABLE books (name VARCHAR(255), address VARCHAR(255))")
database.execute("CREATE TABLE buku (name VARCHAR(255), address VARCHAR(255))")
database.execute("CREATE TABLE user(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(30) NOT NULL, lastname VARCHAR(30) NOT NULL, email VARCHAR(50))")