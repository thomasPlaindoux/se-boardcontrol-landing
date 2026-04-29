import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silence access logs on Heroku

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()
