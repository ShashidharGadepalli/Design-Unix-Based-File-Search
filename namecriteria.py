from criteria import Criteria
from file import File

class Name(Criteria):

    def __init__(self,name:str):
        self._name = name

    def matches(self, file:File):
        return self._name in file.get_name()