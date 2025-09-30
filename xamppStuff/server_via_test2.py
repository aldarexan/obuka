import pymysql

# Connect to the MySQL server
db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
  #  database="example",
    )

# Get a cursor object
cursor = db.cursor()

# Execute the query to get a list of databases
#cursor.execute("SHOW DATABASES")
#cursor.execute("SELECT * FROM users")

data_list = []

# Fetch and print all databases
for database in cursor.fetchall():
    data_list.append(database)  
    print(database)



#server
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class JSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

       
        # Convert the Python dictionary to JSON and send the response
        self.wfile.write(json.dumps(data_list).encode()) #kao lista

if __name__ == "__main__":
    print("Starting the JSON server...")
    server_address = ("localhost", 8000) 
    httpd = HTTPServer(server_address, JSONHandler)
    print(f"Serving JSON data at http://{server_address}:{server_address}")
    httpd.serve_forever()