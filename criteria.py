from abc import ABC,abstractmethod

class Criteria(ABC):
    @abstractmethod
    def matches(self,file):
        pass