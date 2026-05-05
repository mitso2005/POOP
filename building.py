from assets.base import SafetyAsset

# Module Structure: building-specific behavior is isolated here.
class Building:
    def __init__(self, _name, address):
        self._name = _name
        self.address = address
        # Composition: Building owns this internal asset collection.
        self._assets = []
        
    def summary(self):
        print(f'Building Name: {self.name} | Address: {self.address} | Asset Count: {self.asset_count} | Overdue Inspections: {self.get_overdue_assets()}')
        
    def list_items(self):
        print(f'Assets: {self.get_assets}')
        
    def add_asset(self, asset):
        # isinstance(): proper runtime type check for accepted asset types.
        if isinstance(asset, SafetyAsset):
            pass
        else:
            raise TypeError("asset is not an instance of SafetyAsset")
        
        for a in self._assets:
            if asset.__eq__(a):
                raise ValueError('asset already exists in Building')
        
        self._assets.append(asset)
        
    def get_overdue_assets(self):
        # List Comprehension: pythonic filtering for overdue assets.
        return [x for x in self._assets if x.last_inspected == "Never"]
    
    def get_assets_by_type(self, asset_type):
        # List Comprehension + isinstance(): filtered view by concrete type.
        return [x for x in self._assets if isinstance(x, asset_type)]
    
    # __len__: lets Building work with len(building).
    def __len__(self):
        return len(self._assets)
    
    # __str__: human-readable building summary string.
    def __str__(self):
        return f'{self.name} ({self.address}) - {len(self)} assets'
        
    # @classmethod: alternative constructor from dictionary data.
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['address'])
        
    # @property: controlled read access to assets.
    @property
    def get_assets(self):
        return self._assets
    
    # @property: computed, read-only count derived from internal list.
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
        