from criteria import Criteria

class OrCriteria(Criteria):

    def __init__(self, *criteria):
        self._criteria = criteria

    def matches(self, file):
        return any(c.matches(file) for c in self._criteria)


