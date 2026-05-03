from exceptions import InspectionError
from typing import Iterable
from assets.base import SafetyAsset
from assets.devices import FireDoor, FireExtinguisher, SmokeDetector

def print_asset_summary(assets: Iterable[SafetyAsset]):
    print(f'Total Assets: {len(assets)}')
    
    for child in SafetyAsset.__subclasses__():
        instances = 0
        for asset in assets:
            if isinstance(asset, child):
                instances += 1
                asset.describe()
                
        print(f'Total {child.__name__}: {instances}')

def run_all_inspections(assets: Iterable[SafetyAsset]):
    for asset in assets:
        asset.run_inspection()
    
    


