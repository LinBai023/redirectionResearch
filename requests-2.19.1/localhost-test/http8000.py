
import BaseHTTPServer
import ssl

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.headers)
        self.send_response(200)
        self.end_headers()
        self.wfile.write('')

httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()
