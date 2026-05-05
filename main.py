from assets.base import SafetyAsset
from assets.devices import FireDoor, SmokeDetector, FireExtinguisher
from assets.utils import InspectionLog, print_asset_summary, run_all_inspections, print_report
from building import Building
from technician import Technician


if __name__ == "__main__":
    # Practical demo flow:
    # 1) Create building
    factory_1 = Building('Factory_1', '112 Industrial Dr, Richmond')
    factory_2 = Building('Factory_2', '1122 Industrial Dr, Richmond')

    # 2) Validate serials (@staticmethod on SafetyAsset)
    for serial in ['EX-001', 'bad-serial']:
        print(f'{serial} valid: {bool(SafetyAsset.is_valid_serial(serial))}')

    # 3) Add assets (Composition: Building owns its asset list)
    assets_for_factory = [
        FireExtinguisher('EX-001', 'CO2', 'Lobby', 'Never'),
        SmokeDetector('SD-001', 'Ei650', 'Hallway', 'Never'),
        FireDoor('FD-001', 'FD30', 'Exit', 'Never'),
    ]
    for asset in assets_for_factory:
        factory_1.add_asset(asset)

    # 4) Assign technician (Aggregation: Technician references Building)
    tech_1 = Technician('tech_1', 1234)
    tech_1.assign_to(factory_1)
    tech_1.assign_to(factory_2)

    # 5) Run inspections (Polymorphism via shared run_inspection method)
    run_all_inspections(factory_1.get_assets)

    # Extra: show grouped counts via isinstance checks
    print_asset_summary(factory_1.get_assets)

    # 6) Print len(building) (__len__)
    print(len(factory_1))

    # 7) Print building (__str__)
    print(factory_1)

    # 8) Call print_report() (Duck Typing)
    print_report(factory_1)
    log_1 = InspectionLog('Factory 1 Log', factory_1.get_assets)
    print_report(log_1)

    # 9) Print workload
    print(tech_1.get_workload)
    
    