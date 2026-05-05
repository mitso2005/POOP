from typing import Iterable
from assets.base import SafetyAsset

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
        
def print_report(obj):
    # Duck typing: any object with these methods can be reported.
    obj.summary()
    obj.list_items()

class InspectionLog():
    def __init__(self, label: str, records: Iterable):
        self.label = label
        self._records = list(records)
    
    def summary(self):
        print(f'InspectionLog: {self.label} | Total Records: {len(self._records)}')

    def list_items(self):
        for index, record in enumerate(self._records, start=1):
            print(f'{index}. {record}')
        
    
    
    
    


