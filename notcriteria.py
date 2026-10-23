from criteria import Criteria

class NotCriteria(Criteria):

    def __init__(self, criteria):
        self._criteria = criteria

    def matches(self, file):
        return not (self._criteria.matches(file))


