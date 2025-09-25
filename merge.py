
#CRud
import sqlite3

# Connect to (or create) a database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table  (Šema ?)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

# Insert data (hardcoded, neki input?, *arg **kwarg../)
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Alice', 'alice@example.com')) 
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Bob', 'bob@example.com'))

#duplikati? (https://stackoverflow.com/questions/2594829/finding-and-deleting-duplicate-values-in-a-sql-table)

# Commit changes
conn.commit()

# Query data

#drugi pokusaj (via Leo)
sql_command = """
    DELETE FROM users
    WHERE id NOT IN (
    SELECT MIN(id)
    FROM users
    GROUP BY name, email
);
"""
#ne radi..
"""
              DELETE FROM users
WHERE (name, email) IN (
    SELECT name, email
    FROM users
    GROUP BY name, email
    HAVING COUNT(*) > 1
);
               """


conn.commit() #konacno pohranjivanje (nije cistilo bazu.. 😅)

#cursor.execute(sql_command)
#cursor.execute("DELETE FROM users") #wipe all out



cursor.execute("SELECT * FROM users") 

rows = cursor.fetchall()

#izmena plasiranja podataka
data = {}
data_list =[]

for row in rows:
    print(row)  
    data = {
    'id': row[0],
    'name': row[1],
    'email': row[2],
        }
    data_list.append(data)
    

# Close the connection
conn.close()

#server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class JSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Prepare the JSON data
    #    data = {
           # "message": "Hello, world!",
           # "timestamp": "2025-09-24T12:00:00Z" 
           
     #   }

        # Convert the Python dictionary to JSON and send the response
        self.wfile.write(json.dumps(data_list).encode()) #kao lista

if __name__ == "__main__":
    print("Starting the JSON server...")
    server_address = ("localhost", 8000) 
    httpd = HTTPServer(server_address, JSONHandler)
    print(f"Serving JSON data at http://{server_address}:{server_address}")
    httpd.serve_forever()