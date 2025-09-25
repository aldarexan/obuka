#(via  AI)

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class JSONHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Prepare the JSON data
        data = {
            "message": "Hello, world!",
            "timestamp": "2025-09-24T12:00:00Z"
        }

        # Convert the Python dictionary to JSON and send the response
        self.wfile.write(json.dumps(data).encode())

if __name__ == "__main__":
    print("Starting the JSON server...")
    server_address = ("localhost", 8000)
    httpd = HTTPServer(server_address, JSONHandler)
    print(f"Serving JSON data at http://{server_address}:{server_address}")
    httpd.serve_forever()