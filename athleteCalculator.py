import tkinter as tk

class AthleteCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("North Sussex Judo Calculator")

        self.athleteName = tk.Label(root, text="Athlete name:")
        self.athleteName.grid(row=0, column=0, padx=10, pady=10)
        self.athleteNameInput = tk.Entry(root)
        self.athleteNameInput.grid(row=0, column=1, padx=10, pady=10)

        self.memberPlan = tk.Label(root, text="Membership plan:")
        self.memberPlan.grid(row=1, column=0, padx=10, pady=10)
        self.memberPlanVar = tk.StringVar(value="Basic")
        self.memberPlanMenu = tk.OptionMenu(root, self.memberPlanVar, "Basic", "Standard", "Premium")
        self.memberPlanMenu.grid(row=1, column=1, padx=10, pady=10)

        self.trainingSessions = tk.Label(root, text="No. of training sessions per week:")
        self.trainingSessions.grid(row=2, column=0, padx=10, pady=10)
        self.trainingSessionsInput = tk.Entry(root)
        self.trainingSessionsInput.grid(row=2, column=1, padx=10, pady=10)

        self.groupSessions = tk.Label(root, text="No. of group sessions per week:")
        self.groupSessions.grid(row=3, column=0, padx=10, pady=10)
        self.groupSessionsInput = tk.Entry(root)
        self.groupSessionsInput.grid(row=3, column=1, padx=10, pady=10)

        self.additionalTowel = tk.Label(root, text="Towel?")
        self.additionalTowel.grid(row=4, column=0, padx=10, pady=10)
        self.additionalTowelVar = tk.StringVar(value="No")
        self.additionalTowelMenu = tk.OptionMenu(root, self.additionalTowelVar, "Yes", "No")
        self.additionalTowelMenu.grid(row=4, column=1, padx=10, pady=10)

        self.additionalLocker = tk.Label(root, text="Locker?")
        self.additionalLocker.grid(row=5, column=0, padx=10, pady=10)
        self.additionalLockerVar = tk.StringVar(value="No")
        self.additionalLockerMenu = tk.OptionMenu(root, self.additionalLockerVar, "Yes", "No")
        self.additionalLockerMenu.grid(row=5, column=1, padx=10, pady=10)

        self.calculateButton = tk.Button(root, text="Calculate", command=self.calculation)
        self.calculateButton.grid(row=6, column=0, padx=10, pady=10)

        self.athleteNameResult = tk.Label(root, text="")
        self.athleteNameResult.grid(row=8, column=0, padx=10, pady=10)

        self.memberPlanResult = tk.Label(root, text="")
        self.memberPlanResult.grid(row=9, column=0, padx=10, pady=10)

        self.memberTrainingSessionsResult = tk.Label(root, text="")
        self.memberTrainingSessionsResult.grid(row=10, column=0, padx=10, pady=10)

        self.memberGroupSessionsResult = tk.Label(root, text="")
        self.memberGroupSessionsResult.grid(row=11, column=0, padx=10, pady=10)

        self.additionalTowelResult = tk.Label(root, text="")
        self.additionalTowelResult.grid(row=12, column=0, padx=10, pady=10)

        self.additionalLockerResult = tk.Label(root, text="")
        self.additionalLockerResult.grid(row=13, column=0, padx=10, pady=10)

        self.totalCostResult = tk.Label(root, text="")
        self.totalCostResult.grid(row=15, column=0, padx=10, pady=10)

    def calculation(self):
        athleteName = str(self.athleteNameInput.get())
        memberPlan = str(self.memberPlanVar.get())
        trainingSessions = int(self.trainingSessionsInput.get())
        groupSessions = int(self.groupSessionsInput.get())
        additionalTowel = str(self.additionalTowelVar.get())
        additionalLocker = str(self.additionalLockerVar.get())

        try:
            if memberPlan == "Basic":
                membershipCostPerMonth = 15*4
            elif memberPlan == "Standard":
                membershipCostPerMonth = 25*4
            else:
                membershipCostPerMonth = 35*4

        except ValueError:
            self.memberPlanResult.config(text=f"Invalid Input.")

        trainingSessionTotal = (trainingSessions*20)*4
        groupSessionTotal = (groupSessions*10)*4

        if additionalTowel == "Yes":
            additionalTowelCost = 5
        else:
            additionalTowelCost = 0

        if additionalLocker == "Yes":
            additionalLockerCost = 10
        else:
            additionalLockerCost = 0

        totalCost = membershipCostPerMonth + trainingSessionTotal + groupSessionTotal + additionalTowelCost + additionalLockerCost

        self.athleteNameResult.config(text=f"Athlete name: {athleteName}")
        self.memberPlanResult.config(text=f"Membership cost per month: £{membershipCostPerMonth}")
        self.memberTrainingSessionsResult.config(text=f"Training sessions this month: £{trainingSessionTotal}")
        self.memberGroupSessionsResult.config(text=f"Group sessions cost this month: £{groupSessionTotal}")
        self.additionalTowelResult.config(text=f"Additional towel cost: £{additionalTowelCost}")
        self.additionalLockerResult.config(text=f"Additional locker cost: £{additionalLockerCost}")
        self.totalCostResult.config(text=f"Total monthly cost: £{totalCost}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AthleteCalculator(root)
    root.mainloop()