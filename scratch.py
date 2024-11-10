privateSession = 2

#private session calculation
if(privateSession > 5):
    print("Athletes cannot have more than 5 private sessions a week.\nPlease complete the form again.")
else:
    privateSessionCost = float((privateSession * 9.5) * 4)
    print(privateSessionCost)