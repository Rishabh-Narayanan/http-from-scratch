from .header import Header
from .payload import Payload
from .status import Status
from .version import Version


class Response:
    def __init__(self):
        self._status: Status = Status.ok()
        self._version: Version = Version(major=1, minor=1)  # (Major, Minor) as per RFC
        self._headers: dict[str, Header] = {}
        self._payload: Payload = Payload()

    def set_version(self, version: Version):
        self._version = version

    def set_status(self, status: Status):
        self._status = status

    def set_header(self, name: str, value: str):
        self._headers[name] = Header(name, value)

    def unset_header(self, name: str):
        self._headers.pop(name)

    def set_payload(self, data: bytes):
        self._payload.set_data(data)

    def to_bytes(self) -> bytes:
        status = "%s %s" % (
            str(self._version),
            str(self._status),
        )

        headers = "\r\n".join(map(str, self._headers.values()))
        # As per RFC, a CRLF (carriage return and line feed) must split every line.
        # Between the headers and the message body, there must exist an empty line.
        # This is how user agents will determine where the body begins.
        #
        # `encode` converts the string to bytes.
        return str.encode("\r\n".join([status, headers, "\r\n"])) + self._payload.data()
