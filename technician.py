class Technician:
    def __init__(self, name: str, licence_number):
        self.name = name
        self.licence_number = licence_number
        self._assigned_buildings = []
        
    def assign_to(self, building):
        self._assigned_buildings.append(building)
    
    @property
    def get_workload(self):
        workload = []
        for i in self._assigned_buildings:
            workload.append(f'{i.name} ({len(i)} assets)')
            
        return workload