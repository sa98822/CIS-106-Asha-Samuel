#input phase
Lname= input("Enter student last name")
mterm= float(input("Enter midterm score"))
final= float(input("Enter final score"))

#process phase
totalpts= (0.4*mterm + 0.6*final)

#output phase
print("Student last name",Lname)
print ("Total points earned", totalpts)
