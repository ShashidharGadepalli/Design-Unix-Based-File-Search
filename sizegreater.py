from criteria import Criteria
from file import File

class SizeGreter(Criteria):
    def __init__(self,size):
        self._size = size

    def matches(self, file:File):
        return file.get_filesize() >= self._size 