from assets.base import SafetyAsset
from assets.devices import FireDoor, FireExtinguisher, SmokeDetector

def print_asset_summary(assets):
    print(f'Total Assets: {len(assets)}')
    
    for child in SafetyAsset.__subclasses__():
        instances = 0
        for asset in assets:
            if isinstance(asset, child):
                instances += 1
            
    for asset in assets:
        asset.describe()

    
    


