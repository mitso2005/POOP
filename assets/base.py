class SafetyAsset:
    total_assets = 0
    all_serials = []
    
    def __init__(self, serial_number: int, location: str, last_inspected: str = 'Never'):
        self.serial_number = serial_number
        self.location = location
        self.last_inspected = last_inspected
        SafetyAsset.total_assets += 1
        SafetyAsset.all_serials.append(serial_number)
        
    def describe(self):
        print(f"[{self.serial_number}] {self.location} (last inspected: {self.last_inspected})\n")
        
    
        
    