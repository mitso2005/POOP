from abc import ABC, abstractmethod
import re

class SafetyAsset(ABC):
    total_assets = 0
    all_serials = []
    
    def __init__(self, serial_number, location: str, last_inspected: str = 'Never'):
        self.serial_number = serial_number
        self.location = location
        self.last_inspected = last_inspected
        SafetyAsset.total_assets += 1
        SafetyAsset.all_serials.append(serial_number)
        
    @abstractmethod
    def run_inspection(self):
        pass
    
    @staticmethod
    def is_valid_serial(serial):
        return re.fullmatch(r"[A-Z]{2}-\d{3,}", serial)
        
    def describe(self):
        print(f"[{self.serial_number}] {self.location} (last inspected: {self.last_inspected})\n")
        
    def __eq__(slef, other):
        if not isinstance(other, SafetyAsset):
            raise(NotImplemented) 
        return slef.serial_number == other.serial_number
    
    def __str__(self):
        return f'{self.__class__.__name__} {self.serial_number} at {self.location}'
    
    def __repr__(self):
        return f'{self.__class__.__name__}(serial=\'{self.serial_number}\')'