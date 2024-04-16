class Header:
    def __init__(self, name: str, value: str):
        self._name = name
        self._value = value

    def matches(self, name: str) -> bool:
        return name == self._name

    def set_value(self, value: str):
        self._value = value

    def __str__(self):
        return "%s: %s" % (self._name, self._value)
