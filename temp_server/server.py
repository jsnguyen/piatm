from http.server import BaseHTTPRequestHandler, HTTPServer
from get_temp import get_temp
import json

class S(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        if self.path == '/':
            self.wfile.write("<html><body><h1>hi!</h1></body></html>".encode())
        elif self.path == '/temp/':
            temp = {'temp':get_temp()}
            self.wfile.write(json.dumps(temp).encode())

    def do_POST(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>".encode())

def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('10.0.0.111', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
