from assets.base import SafetyAsset
from exceptions import InspectionError
import datetime

# Module Structure: concrete device types live in a dedicated module.
class FireExtinguisher(SafetyAsset):
    VALID_TYPES = {"CO2", "Dry Powder", "Wet Chemical", "Water"}
    total = 0
    
    def __init__(self, serial_number, extinguisher_type , location, last_inspected):
        # super().__init__(): extend parent setup before child-specific fields.
        super().__init__(serial_number, location, last_inspected) 
        self.feat = extinguisher_type
        
        FireExtinguisher.total += 1
        
    def run_inspection(self):
        if self.feat not in self.VALID_TYPES:
            raise(InspectionError)
        else:
            print('VALID TYPE - FireExtinguisher Inspection Passed')
        
        self.last_inspected = datetime.date.today()
    
    def describe(self):
        print(f"[{self.serial_number}] type: {self.feat} {self.location} (last inspected: {self.last_inspected})")
        
class SmokeDetector(SafetyAsset):
    total = 0
    
    def __init__(self, serial_number, detector_model, location, last_inspected):
        # super().__init__(): reuse shared base initialization.
        super().__init__(serial_number, location, last_inspected) 
        self.feat = detector_model
        
        SmokeDetector.total += 1
        
    def run_inspection(self):
        print('BEEP - SmokeDetector Inspection Passed')
    
        self.last_inspected = datetime.date.today()
    
    def describe(self):
        print(f"[{self.serial_number}] type: {self.feat} {self.location} (last inspected: {self.last_inspected})")
       
class FireDoor(SafetyAsset):
    total = 0
    
    def __init__(self, serial_number, door_rating, location, last_inspected):
        # super().__init__(): inherit common SafetyAsset state.
        super().__init__(serial_number, location, last_inspected) 
        self.feat = door_rating
        
        FireDoor.total += 1
        
    def run_inspection(self):
        print('OPEN AND CLOSE - FireDoor Inspection Passed')

        self.last_inspected = datetime.date.today()

    def describe(self):
        print(f"[{self.serial_number}] type: {self.feat} {self.location} (last inspected: {self.last_inspected})")