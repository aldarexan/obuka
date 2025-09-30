import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1", #localhost
    port=3306,
    user="root",
    password=""
)

cursor = db.cursor()
#cursor.execute("SELECT * FROM your_database.your_table") #test.db
cursor.execute("SELECT * FROM example.users") #example.db
results = cursor.fetchall()

db.commit()
for row in results:
    print(row)

db.close()