# Essay 1
purchasePrice = 25000
useFullLife = 5
residualValue = 2000
anualDeprciation = (purchasePrice - residualValue) / useFullLife
print('Anual Depriciation ', anualDeprciation)
depriciationOverTwoYears = anualDeprciation * 2
print('Depriciation Over Two Years', depriciationOverTwoYears)
remainingAssetValue = purchasePrice - depriciationOverTwoYears
print('Remaining Assets', remainingAssetValue)
assetsValueAfterTwoYears = purchasePrice - (depriciationOverTwoYears * 2)
print('Asset Value After Two Years', assetsValueAfterTwoYears)




# Essay 2
name = 'nyimansata'
aster = '**********'
for i in range(1, 10):## or the name can be used as well
    print(name[:i].capitalize())