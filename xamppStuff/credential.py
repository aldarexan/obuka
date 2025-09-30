import pymysql

# Connect to the MySQL server
connection = pymysql.connect(
    host='localhost',
    user='root',
    password=''
)

# Create a cursor object
cursor = connection.cursor()

# Create a new user
username = 'my_user'
password = 'my_password'
cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")

# Grant permissions to the new user
database_name = 'my_database'
cursor.execute(f"GRANT ALL PRIVILEGES ON {database_name}.* TO '{username}'@'localhost'")
cursor.execute("FLUSH PRIVILEGES")

print(f"User '{username}' created and granted access to '{database_name}' database.")

# Close the connection
connection.close()