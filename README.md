# liefwerk.dev

## To do
- [] make a local dev server in python

```python
#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import unquote

class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = unquote(self.path)
        if '?' in path:
            path = path.split('?')[0]
        
        if path.endswith('/'):
            path = path + 'index.html'
        elif not os.path.splitext(path)[1]:
            html_path = path + '.html'
            if os.path.exists(html_path.lstrip('/')):
                self.path = html_path
        
        return super().do_GET()

PORT = 8000
with socketserver.TCPServer(("", PORT), CleanURLHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
```