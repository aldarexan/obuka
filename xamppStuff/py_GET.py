import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    port=3306,
 #   user="root",
 #  password=""
)


# XAMPP server connection details
db_host = 'localhost' #localhost
db_user = '' #your_username
db_password = '' #your_password
db_name = 'example' #your_database_name

# Port for the server
PORT = 8000  #ovo?


cursor = db.cursor()

cursor.execute("SELECT * FROM users") #example.db
results = cursor.fetchall()

for row in results:
    print(row)

#db.commit()
db.close()