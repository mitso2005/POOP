from assets.base import SafetyAsset
from assets.devices import FireDoor, SmokeDetector, FireExtinguisher
from assets.utils import print_asset_summary, run_all_inspections


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
    
    
    