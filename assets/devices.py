from assets.base import SafetyAsset

class FireExtinguisher(SafetyAsset):
    def __init__(self, serial_number, extinguisher_type, location, last_inspected):
        super().__init__(serial_number, location, last_inspected) 
        self.feat = extinguisher_type
    
    def describe(self):
        print(f"[{self.serial_number}] type: {self.feat} {self.location} (last inspected: {self.last_inspected})")
        
class SmokeDetector(SafetyAsset):
    def __init__(self, serial_number, detector_model, location, last_inspected):
        super().__init__(serial_number, location, last_inspected) 
        self.feat = detector_model
    
    def describe(self):
        print(f"[{self.serial_number}] type: {self.feat} {self.location} (last inspected: {self.last_inspected})")
       
class FireDoor(SafetyAsset):
    def __init__(self, serial_number, door_rating, location, last_inspected):
        super().__init__(serial_number, location, last_inspected) 
        self.feat = door_rating
    
    def describe(self):
        print(f"[{self.serial_number}] type: {self.feat} {self.location} (last inspected: {self.last_inspected})")