import tkinter as tk

#the calculator is contained within one class
class AthleteCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("North Sussex Judo Calculator")

        #defining all the inputs/labels for the GUI
        self.athleteName = tk.Label(root, text="Athlete name:")
        self.athleteName.grid(row=0, column=0, padx=10, pady=10)
        self.athleteNameInput = tk.Entry(root)
        self.athleteNameInput.grid(row=0, column=1, padx=10, pady=10)

        self.trainingPlan = tk.Label(root, text="Training plan:")
        self.trainingPlan.grid(row=1, column=0, padx=10, pady=10)
        self.trainingPlanVar = tk.StringVar(value="Beginner")
        self.trainingPlanMenu = tk.OptionMenu(root, self.trainingPlanVar, "Beginner", "Intermediate", "Elite")
        self.trainingPlanMenu.grid(row=1, column=1, padx=10, pady=10)

        self.currentWeight = tk.Label(root, text="Weight in kg to nearest whole:")
        self.currentWeight.grid(row=2, column=0, padx=10, pady=10)
        self.currentWeightInput = tk.Entry(root)
        self.currentWeightInput.grid(row=2, column=1, padx=10, pady=10)

        self.competitionWeightCategory = tk.Label(root, text="Competition weight category:")
        self.competitionWeightCategory.grid(row=3, column=0, padx=10, pady=10)
        self.competitionWeightCategoryVar = tk.StringVar(value="Heavyweight")
        self.competitionWeightCategoryMenu = tk.OptionMenu(root, self.competitionWeightCategoryVar, "Heavyweight", "Light-Heavyweight",
                                                           "Middleweight", "Light-Middleweight", "Lightweight", "Flyweight")
        self.competitionWeightCategoryMenu.grid(row=3, column=1, padx=10, pady=10)

        self.competitions = tk.Label(root, text="No. of competitions this month:")
        self.competitions.grid(row=4, column=0, padx=10, pady=10)
        self.competitionsInput = tk.Entry(root)
        self.competitionsInput.grid(row=4, column=1, padx=10, pady=10)

        self.privateSession = tk.Label(root, text="No. of private sessions per week:")
        self.privateSession.grid(row=5, column=0, padx=10, pady=10)
        self.privateSessionInput = tk.Entry(root)
        self.privateSessionInput.grid(row=5, column=1, padx=10, pady=10)

        self.calculateButton = tk.Button(root, text="Calculate", command=self.calculation)
        self.calculateButton.grid(row=6, column=0, padx=10, pady=10)

        self.athleteNameResult = tk.Label(root, text="")
        self.athleteNameResult.grid(row=8, column=0, padx=10, pady=10)

        self.trainingPlanResult = tk.Label(root, text="")
        self.trainingPlanResult.grid(row=9, column=0, padx=10, pady=10)

        self.currentWeightResult = tk.Label(root, text="")
        self.currentWeightResult.grid(row=10, column=0, padx=10, pady=10)

        self.competitionWeightResult = tk.Label(root, text="")
        self.competitionWeightResult.grid(row=11, column=0, padx=10, pady=10)

        self.competitionCostResult = tk.Label(root, text="")
        self.competitionCostResult.grid(row=12, column=0, padx=10, pady=10)

        self.privateSessionResult = tk.Label(root, text="")
        self.privateSessionResult.grid(row=13, column=0, padx=10, pady=10)

        self.totalCostResult = tk.Label(root, text="")
        self.totalCostResult.grid(row=15, column=0, padx=10, pady=10)

    def calculation(self):
        #setting the variables used in the function
        athleteName = str(self.athleteNameInput.get())
        trainingPlan = str(self.trainingPlanVar.get())
        try:
            currentWeight = int(self.currentWeightInput.get())
        except ValueError:
            self.currentWeightResult.config(text="Current weight category: Invalid value.\nPlease enter a whole number.")
        competitionWeightCategory = str(self.competitionWeightCategoryVar.get())
        try: 
            competitions = int(self.competitionsInput.get())
        except ValueError:
            self.competitionCostResult.config(text="Cost of competitions entered this month: Invalid value.\nPlease enter a whole number.")
        try:
            privateSession = int(self.privateSessionInput.get())
        except ValueError:
            self.privateSessionResult.config(text=f"Cost of private sessions this month: Invalid value.\nPlease enter a whole number.")

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
            self.competitionCostResult.config(text="Beginners cannot enter competitions.\nPlease complete the form again.")
        else:
            competitionCost = competitions * 22

        #private session calculation
        if(privateSession > 5):
            self.privateSessionResult.config(text="Athletes cannot have more than 5 private sessions a week.\nPlease complete the form again.")
        else:
            privateSessionCost = float((privateSession * 9.5) * 4)

        #total cost of all values
        totalCost = float(trainingCostPerMonth + competitionCost + privateSessionCost)

        #configuring the result values after button click
        self.athleteNameResult.config(text=f"Athlete name: {athleteName}")
        self.trainingPlanResult.config(text=f"Training plan cost per month: £{trainingCostPerMonth:.2f}")
        self.currentWeightResult.config(text=f"Current weight category: {currentWeightCategory}")
        self.competitionWeightResult.config(text=f"Competition weight category: {competitionWeightCategory}")
        self.competitionCostResult.config(text=f"Cost of competitions entered this month: £{competitionCost:.2f}")
        self.privateSessionResult.config(text=f"Cost of private sessions this month: £{privateSessionCost:.2f}")
        self.totalCostResult.config(text=f"Total monthly cost: £{totalCost:.2f}")

#initialising the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = AthleteCalculator(root)
    root.mainloop()