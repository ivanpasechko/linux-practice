from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success", "method": "GET"}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/post':
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success", "method": "POST"}')
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        if self.path == '/put':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success", "method": "PUT"}')
        else:
            self.send_response(404)
            self.end_headers()

server = HTTPServer(('0.0.0.0', 5000), SimpleHandler)
print("Server starting on port 5000...")
server.serve_forever()
