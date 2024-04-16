class Status:
    def __init__(self, code: int, reason: str | None):
        self._code = code
        self._reason = reason

    def set_reason(self, reason: str):
        self._reason = reason

    def __str__(self):
        return "%d %s" % (self._code, self._reason)

    def ok():
        return Status(200, "OK")
    
    def see_other():
        return Status(303, "See Other")

    def bad_request():
        return Status(400, "Bad Request")

    def not_found():
        return Status(404, "Not Found")

    def internal_server_error():
        return Status(500, "Internal Server Error")
    
    def not_implemented():
        return Status(501, "Not Implemented")

    def http_version_not_supported():
        return Status(505, "HTTP Version Not Supported")
