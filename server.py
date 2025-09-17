#!/usr/bin/env python3
"""
Simple HTTP server for serving static HTML files
"""
import http.server
import socketserver
import os
from pathlib import Path

# Server configuration - handled in main() function

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to serve files from
        super().__init__(*args, directory="3.0  copy", **kwargs)
    
    def end_headers(self):
        # Add headers to prevent caching for development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        # Handle root path - redirect to main page
        if self.path == '/':
            self.path = '/h3.0.html'
        super().do_GET()

def main():
    # Change to project directory
    os.chdir(Path(__file__).parent)
    
    # Get port and host from environment
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    print(f"Starting server on {host}:{port}")
    print(f"Serving files from: {os.path.abspath('3.0  copy')}")
    print("Available pages:")
    print(f"  - http://localhost:{port}/ (main heritage marketplace)")
    print(f"  - http://localhost:{port}/h3.0.html (heritage marketplace)")
    print(f"  - http://localhost:{port}/h3.0.1.html (AI travel planner)")
    
    try:
        with socketserver.TCPServer((host, port), CustomHTTPRequestHandler) as httpd:
            # Allow port reuse
            httpd.allow_reuse_address = True
            print(f"Server started at http://{host}:{port}")
            httpd.serve_forever()
    except OSError as e:
        if e.errno == 98:  # Address already in use
            # Only try alternative ports in development (when PORT env var is not set)
            if "PORT" not in os.environ:
                print(f"Port {port} is already in use. Trying to find an available port...")
                import socket
                # Try to find an available port
                for port_try in range(port + 1, port + 100):
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                            s.bind((host, port_try))
                            port = port_try
                            break
                    except OSError:
                        continue
                print(f"Using port {port} instead")
                with socketserver.TCPServer((host, port), CustomHTTPRequestHandler) as httpd:
                    httpd.allow_reuse_address = True
                    print(f"Server started at http://{host}:{port}")
                    httpd.serve_forever()
            else:
                print(f"Port {port} is already in use and PORT environment variable is set. Exiting for deployment restart.")
                raise
        else:
            raise
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()