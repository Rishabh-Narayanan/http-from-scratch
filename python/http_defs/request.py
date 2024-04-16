from http_defs.header import Header
from http_defs.method import Method
from http_defs.payload import Payload
from http_defs.version import Version


class Request:
    def __init__(self):
        self._path: str = "/"
        self._method: Method = Method("GET")
        self._version: Version = Version(major=1, minor=1)  # (Major, Minor) as per RFC
        self._headers: dict[str, Header] = {}
        self._payload: Payload = Payload()
    
    def path(self) -> str:
        return self._path
    
    def method(self) -> Method:
        return self._method
    
    def version(self) -> Version:
        return self._version

    def from_bytes(data: bytes) -> "Request | None":
        request = Request()

        [req_line, *lines] = data.decode().split("\r\n")
        # Request line is the most important line. It is of the following form as per RFC:
        # METHOD PATH HTTP-Version. For example:
        # GET /index.html HTTP/1.1
        # POST /custom-route HTTP/1.1
        request_tokens = req_line.split(" ")
        request._method = Method(request_tokens[0])
        request._path = "/" if len(request_tokens) < 2 else request_tokens[1]
        if len(request_tokens) >= 3:
            request._version = Version.from_str(request_tokens[2])
        if not request._version or not request._path:
            return None

        # Parse Request Headers
        i = 0
        # Empty line = End of headers. Following lines would be request body
        while i < len(lines) and lines[i] != "":
            header: list[str] = lines[i].split(": ")
            if len(header) != 2:
                return None
            h, v = header[0].strip(), header[1].strip()
            request._headers[h] = Header(h, v)
            i += 1

        request._payload.set_data(str.encode("\r\n".join(lines[(i + 1) :])))
        return request
