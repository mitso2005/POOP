from assets.base import SafetyAsset
from assets.devices import FireDoor, FireExtinguisher, SmokeDetector

def print_asset_summary(assets):
    print(f'Total Assets: {SafetyAsset.total_assets}')
    
    for subclass in SafetyAsset.__subclasses__():
        print(f'No. {subclass.__name__}: {subclass.total}')
        for asset in assets:
            if isinstance(asset, subclass):
                asset.describe()

    
    


