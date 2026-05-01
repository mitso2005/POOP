from assets.base import SafetyAsset
from assets.devices import FireDoor, SmokeDetector

test_1 = FireDoor(1235, 'Sturdy', 'Melbourne', '23/04/23')
test_2 = SmokeDetector(1235, 'Smokey', 'Melbourne', '23/04/23')

test_1.describe()
test_2.describe()

print(SafetyAsset.total_assets)
print(SafetyAsset.all_serials)