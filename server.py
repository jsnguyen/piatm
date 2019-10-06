from http.server import BaseHTTPRequestHandler, HTTPServer
from sensors import get_all_sensor_data
import json

class S(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()
        if self.path == '/':
            self.wfile.write(json.dumps(get_all_sensor_data()).encode())

def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('10.0.0.66', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
