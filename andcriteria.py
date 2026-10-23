from criteria import Criteria

class AndCriteria(Criteria):

    def __init__(self, *criteria):
        self._criteria = criteria

    def matches(self, file):
        return all(c.matches(file) for c in self._criteria)


