class Method:
    def __init__(self, method: str):
        self._method = method
    
    def isGET(self):
        return self._method == "GET"
    
    def isHEAD(self):
        return self._method == "HEAD"
    
    def isPOST(self):
        return self._method == "POST"
    
    def isDELETE(self):
        return self._method == "DELETE"
    
    def isPATCH(self):
        return self._method == "PATCH"
        