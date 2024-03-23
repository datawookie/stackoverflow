from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("index.html", "rb") as file:
            self.wfile.write(file.read())


httpd = HTTPServer(("0.0.0.0", 3000), SimpleHTTPRequestHandler)
httpd.serve_forever()
