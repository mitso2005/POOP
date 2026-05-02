from assets.base import SafetyAsset
from assets.devices import FireDoor, SmokeDetector, FireExtinguisher
from assets.utils import print_asset_summary


if __name__ == "__main__":
    assets = [
        FireExtinguisher("EX-001", "CO2", "Lobby", "Never"),
        SmokeDetector("SD-001", "Ei650", "Hallway", "Never"),
        FireDoor("FD-001", "FD30", "Exit", "Never")
    ]
    
    print(SafetyAsset.total_assets)
    print(SafetyAsset.all_serials)

    print_asset_summary(assets)
    