import os
import socket

from http_defs.request import Request
from http_defs.response import Response
from http_defs.status import Status
from http_defs.version import Version


# An HTTP 1.1 Server implementation that can handle basic requests and serve resources.
class Server:
    def __init__(self, host: str, port: int, max_connections: int, buffer_size_kb: int):
        self.host = host
        self.port = port
        self.max_connections = max_connections
        self.buffer_size_kb = buffer_size_kb
        self.socket: socket.socket = None

    def start_server(self):
        # Connect over IPv4 (AF_INET) and over TCP (SOCK_STREAM)
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(self.max_connections)

        print("Accepting connections at %s" % str(self.socket.getsockname()))

        while True:
            conn, addr = self.socket.accept()
            raw_data = conn.recv(self.buffer_size_kb * 1024)  # 1 kb = 1024 bytes
            req: Request = Request.from_bytes(raw_data)
            res: Response = Response()
            self.handle_request(req, res)
            conn.sendall(res.to_bytes())
            conn.close()

    def close_server(self):
        print("Closing server and connections")
        self.socket.close()

    def handle_request(self, req: Request | None, res: Response):
        # req is None if the parsing from the byte stream failed
        if req is None:
            res.set_status(Status.bad_request())
            return

        # Current implementation only supports HTTP version 1.1
        if req.version().major() != 1 and req.version().minor() != 1:
            res.set_status(Status.http_version_not_supported())
            return

        res.set_version(Version(major=1, minor=1))
        res.set_status(Status.ok())

        # Read resource from file
        resource = req.path().strip("/")

        # Example of a redirect. Let all requests to / go to /index.html
        if resource == "":
            res.set_status(Status.see_other())
            res.set_header("Location", "/index.html")
        elif os.path.exists(resource):
            with open(resource, "rb") as f:
                response_body = f.read()
                if resource.endswith(".html"):
                    res.set_header("Content-Type", "text/html")
                elif resource.endswith(".png"):
                    res.set_header("Content-Type", "image/png")
                elif resource.endswith(".css"):
                    res.set_header("Content-Type", "text/css")
                res.set_payload(response_body)
        else:
            res.set_status(Status.not_found())
            with open("404.html", "rb") as f:
                res.set_header("Content-Type", "text/html")
                res.set_payload(f.read())
