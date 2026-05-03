from assets.base import SafetyAsset

class Building:
    def __init__(self, _name, address):
        self._name = _name
        self.address = address
        self._assets = []
        
    def add_asset(self, asset):
        if isinstance(asset, SafetyAsset):
            pass
        else:
            raise TypeError("asset is not an instance of SafetyAsset")
        
        for a in self._assets:
            if asset.__eq__(a):
                raise ValueError('asset already exists in Building')
        
        self._assets.append(asset)
        
    def get_overdue_assets(self):
        return [x for x in self._assets if x.last_inspected == "Never"]
    
    def get_assets_by_type(self, asset_type):
        return [x for x in self._assets if isinstance(x, asset_type)]
        
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['address'])
        
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