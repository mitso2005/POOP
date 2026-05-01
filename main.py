from assets.base import SafetyAsset

test_1 = SafetyAsset(1235, 'Melbourne', '23/04/23')
test_2 = SafetyAsset(1235, 'Melbourne', '23/04/23')

test_1.describe()

print(SafetyAsset.total_assets)
print(SafetyAsset.all_serials)