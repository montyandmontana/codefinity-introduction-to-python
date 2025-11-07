#1
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#2
deli_dept = [meat, cheese, condiment]

#3
if "Ham" in meat:
    if meat[2] <100:
        meat[2] = 100         

#4
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#5
deli_dept.remove(condiment)

#6
deli_dept.sort()

print("Initial Deli List:", deli_dept)
print("Updated Deli List:",deli_dept)