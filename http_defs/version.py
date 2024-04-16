class Version:
    def __init__(self, major: int, minor: int):
        self._major = major
        self._minor = minor

    def from_str(text: str) -> "Version | None":
        if not text.startswith("HTTP/"):
            return None

        tokens = text[5:].split(".")
        if len(tokens) != 2 or not tokens[0].isdigit() or not tokens[1].isdigit():
            return None

        return Version(major=int(tokens[0]), minor=int(tokens[1]))

    def major(self):
        return self._major

    def minor(self):
        return self._minor

    def set_major(self, major: int):
        self._major = major

    def set_minor(self, minor: int):
        self._minor = minor

    def __str__(self):
        return "HTTP/%d.%d" % (self._major, self._minor)
