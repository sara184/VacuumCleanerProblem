def printInfo(loc):
  print("location" + loc + "is Dirty")
  print("Cost for Cleaning" + loc + "has been cleaned.")
  print("Location" + loc + "has been cleaned")


def vacuumcleaner(goalState, currentstate, loc):
  print("Goal State Required:",goalState)
  print("vacuum is placed in location" + loc)


  totalCost = 0

  while(currentstate != goalState):
    if(loc == "A"):
      if(currentstate["A"] == 1):
        currentstate["A"] = 0
        totalCost += 1
        printInfo("A")

      if(currentstate["B"] == 1 or currentstate["C"] == 1):
        print("Moving right to a location B.\nCost for moving Right: 1")
        loc = "B"
        totalCost += 1


    elif(loc == "B"):
      if(currentstate["B"]==1):
        currentstate["B"] = 0
        totalCost += 1
        printInfo("B")


      if(currentstate["A"] == 1):
        print("Moving left to the location A.\nCost for moving Left: 1")
        loc="A"
        totalCost += 1

      elif(currentstate["C"] == 1):
        print("Moving to the location C.\nCost for moving Right: 1")
        loc = "C"
        totalCost += 1

    elif(loc == "C"):
      if(currentstate["C"] == 1):
        currentstate["C"] = 0
        totalCost += 1

  print("Goal State:", currentstate)
  return totalCost

goalState = {"A": 0,"B": 0,"C": 0}
currentstate = {"A":-1, "B": -1,"C": -1}

loc = input("Enter location of vaccum (A/B/C):");
currentstate["A"] = int(input("Enter status of A(0/1):"))
currentstate["B"] = int(input("Enter status of B (0/1):"))
currentstate["C"] = int(input("Enter status of C (0/1):"))

totalCost = vacuumcleaner(goalState,currentstate,loc)
print("Performance of Measurement", totalCost)