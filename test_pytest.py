def calculation():
        #setting the variables used in the function
        athleteName = "Lewis"
        trainingPlan = "Beginner"
        currentWeight = 80
        competitionWeightCategory = "Heavyweight"
        competitions = 0
        privateSession = 1

        #training plan calculation
        if(trainingPlan == "Beginner"):
            trainingCostPerMonth = 25*4
        elif(trainingPlan == "Intermediate"):
            trainingCostPerMonth = 30*4
        else:
            trainingCostPerMonth = 35*4

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

        #decision/calculation on competitions based on training plan level
        if(trainingPlan == "Beginner") and (competitions > 0):
            "Beginners cannot enter competitions.\nPlease complete the form again."
        else:
            competitionCost = competitions * 22

        #private session calculation
        if(privateSession > 5):
            "Athletes cannot have more than 5 private sessions a week.\nPlease complete the form again."
        else:
            privateSessionCost = float((privateSession * 9.5) * 4)

        #total cost of all values
        totalCost = float(trainingCostPerMonth + competitionCost + privateSessionCost)

        return totalCost


def test():
    #training cost 100 + private session cost 38
    assert calculation() == 138
    