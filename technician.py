# Module Structure: technician behavior and workload logic live here.
class Technician:
    def __init__(self, name: str, licence_number):
        self.name = name
        self.licence_number = licence_number
        # Aggregation: references to buildings are shared, not owned/destroyed.
        self._assigned_buildings = []
        
    def assign_to(self, building):
        self._assigned_buildings.append(building)
    
    @property
    def get_workload(self):
        workload = []
        for i in self._assigned_buildings:
            workload.append(f'{i.name} ({len(i)} assets)')
            
        return workload