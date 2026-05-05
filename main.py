from assets.base import SafetyAsset
from assets.devices import FireDoor, SmokeDetector, FireExtinguisher
from assets.utils import InspectionLog, print_asset_summary, run_all_inspections, print_report
from building import Building
from technician import Technician


if __name__ == "__main__":
    assets_1 = [
        FireExtinguisher("EX-001", "CO2", "Lobby", "Never"),
        SmokeDetector("SD-001", "Ei650", "Hallway", "Never"),
        FireDoor("FD-001", "FD30", "Exit", "Never")
    ]
    
    assets_2 = [
        FireExtinguisher("EX-021", "C4O2", "Room", "Never"),
        SmokeDetector("SD-011", "Ei64550", "Stairs", "Never"),
        FireDoor("FD-041", "F5D30", "Outside", "Never")
    ]
    
    print(SafetyAsset.total_assets)
    print(SafetyAsset.all_serials)

    print_asset_summary(assets_2)
    run_all_inspections(assets_1)
    
    factory_1 = Building('Factory_2', '112 Industrial Dr, Richmond')
    factory_2 = Building('Factory_2', '1122 Industrial Dr, Richmond')
    print(factory_1.asset_count)
    factory_1.add_asset(FireDoor("FD-041", "F5D30", "Outside", "Never"))
    factory_1.add_asset(SmokeDetector("SD-011", "Ei64550", "Stairs", "Never"))
    print(factory_1.asset_count)
    
    factory_1.name = 'factory_1'
    print(factory_1.name)
    
    if SafetyAsset.is_valid_serial('EX-001'):
        print('yes')
        
    tower = Building.from_dict({"name": "Riverside Tower", "address": "42 Fire Lane"})
    print(tower.name)
    
    print(f'{factory_1.get_overdue_assets()}')
    print(factory_1.get_assets_by_type(SmokeDetector))
    
    print(assets_2[0])
    print(assets_1[1].__repr__())
    
    print(factory_1)
    
    tech_1 = Technician('tech_1', 1234)
    
    tech_1.assign_to(factory_1)
    tech_1.assign_to(factory_2)
    
    print(tech_1.get_workload)
    
    print_report(tower)
    print_report(factory_1)
    
    log_1 = InspectionLog('test', assets_2)
    print_report(log_1)
    
    