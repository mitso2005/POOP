class Asset:
    def __init__(self, serial_number: int, location: str, last_inspected: str = 'Never'):
        self.serial_number = serial_number
        self.location = location
        self.last_inspected = last_inspected
        
    def describe(self):
        print(f"[{self.serial_number}] {self.location} (last inspected: {self.last_inspected})\n")
        
    