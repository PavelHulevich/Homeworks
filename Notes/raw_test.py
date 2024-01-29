class MySuperType:

    def __init__(self, value):
        self.value = value

    def _get_length(self):
        match self.value:
            case str():
                return len(self.value)
            case dict():
                return len(self.value.keys()) * 2
            case int():
                return ...

    def __gt__(self, other):
        if self._get_length() > other._get_length():
            return True
        else: return False

    def __lt__(self, other):
        pass


d = MySuperType({'a': 1})
s = MySuperType('str')
print(d.value)
print(s._get_length())

print(d > s)