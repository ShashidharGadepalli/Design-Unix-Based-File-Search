from criteria import Criteria
from file import File

class Extension(Criteria):

    def __init__(self,extension):
        self._extension = extension

    def matches(self, file:File):
        return self._extension == file.get_extension()