#!/usr/bin/env python3
import http.server
import socketserver
import os
from pathlib import Path
from urllib.parse import unquote

ROOT_DIR = Path(__file__).resolve().parent.parent

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def do_GET(self):
        path = unquote(self.path)
        if '?' in path:
            path = path.split('?')[0]
        
        if path.endswith('/'):
            path = path + 'index.html'
        elif not os.path.splitext(path)[1]:
            html_path = path + '.html'
            if (ROOT_DIR / html_path.lstrip('/')).exists():
                self.path = html_path
        
        return super().do_GET()

PORT = 8002
with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()