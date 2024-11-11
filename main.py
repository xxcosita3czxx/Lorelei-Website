import http.server
import socketserver
import os
import time

PORT = 25532
httpd = None
observer = None

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)

    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_server():
    global httpd, observer
    handler = MyHttpRequestHandler

    try:
        httpd = socketserver.TCPServer(("", PORT), handler)
        print(f"Serving on port {PORT}")

        httpd.serve_forever()
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print("Address already in use. Retrying...")
            time.sleep(5)  # Wait before retrying
            start_server()
    except KeyboardInterrupt:
        print("Shutting down server...")
    finally:
        stop_server()

def stop_server():
    global httpd, observer
    if httpd:
        httpd.server_close()  # Ensure the server is properly closed

if __name__ == "__main__":
    start_server()
