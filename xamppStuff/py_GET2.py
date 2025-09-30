import http.server
import socketserver
import urllib.parse
import mysql.connector

# XAMPP server connection details
db_host = 'localhost' #localhost
db_user = '' #your_username
db_password = '' #your_password
db_name = 'example' #your_database_name

# Port for the server
PORT = 8000  #ovo?

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL to get the query parameters
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)

        schema_name = query_params.get('users', [None]) #'schema_name'

        if schema_name:
            try:
                # Connect to the XAMPP server database
                db = mysql.connector.connect(
                    host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                )
                cursor = db.cursor()

                # Create the schema
                create_schema_query = f"CREATE SCHEMA `{schema_name}`;"
                cursor.execute(create_schema_query)
                db.commit()

                # Send a success response
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"Schema '{schema_name}' created successfully.".encode('utf-8'))

            except mysql.connector.Error as error:
                self.send_response(500)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f"Error: {error}".encode('utf-8'))

            finally:
                if 'db' in locals() and db.is_connected():
                    cursor.close()
                    db.close()

        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Please provide a schema name in the GET request.".encode('utf-8'))

# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
    