class Payload:
    def __init__(self):
        self._data: bytes = "".encode()
    
    def set_data(self, data: bytes):
        self._data = data
    
    def data(self) -> bytes:
        return self._data
