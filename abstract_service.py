from abc import ABCMeta, abstractmethod
class AbstractService(metaclass=ABCMeta):
    
    @abstractmethod
    def search_element(self, element):
        pass
    
    @abstractmethod
    def validate_date(self):
        pass
    
    @abstractmethod
    def update_date(self):
        pass
    
    @abstractmethod
    def add_notes(self, notes):
        pass