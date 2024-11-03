currentWeightInput = "eighty"
try: 
    currentWeight = int(currentWeightInput)
except:
    print("Invalid value.")

#decision on weight class depending on input
if(currentWeight > 100):
    currentWeightCategory = "Heavyweight"
elif((currentWeight <= 100) and (currentWeight > 90)):
    currentWeightCategory = "Light-Heavyweight"
elif((currentWeight <= 90) and (currentWeight > 81)):
    currentWeightCategory = "Middleweight"
elif((currentWeight <= 81) and (currentWeight > 73)):
    currentWeightCategory = "Light-Middleweight"
elif((currentWeight <= 73) and (currentWeight > 66)):
    currentWeightCategory = "Lightweight"
else:
    currentWeightCategory = "Flyweight"

print(currentWeightCategory)