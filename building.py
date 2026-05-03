from assets.base import SafetyAsset, __eq__
from exceptions import InspectionError

class Building:
    def __init__(self, _name, address, _assets: list[SafetyAsset]):
        self._name = _name
        self.address = address
        self._assets = _assets
        
    def add_asset(self, asset):
        if isinstance(asset, SafetyAsset):
            pass
        else:
            raise(print('asset is not an instance of SafetyAsset'))
        
        for a in self._assets:
            if asset.__eq__(a):
                raise(print('asset already exists in Building'))
        
        self._assets.append(asset)
        
    @property
    def get_assets(self):
        return self._assets
    
    @property
    def asset_count(self):
        return len(self._assets)
    
    # name getter
    @property
    def name(self):
        return self._name
    
    # name setter
    @name.setter
    def name(self, new_name):
        if new_name == '':
            raise ValueError('Cannot assign empty name to Building')
        self._name = new_name