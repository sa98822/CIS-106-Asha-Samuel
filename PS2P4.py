#input phase
make=input("Make:")
model= input("Model:")
msrp= float(input("msrp: $"))
discpercent= float(input("Enter the discount percent in decimal form"))


#process phase
amtoff= (msrp * discpercent)
discprice= msrp-amtoff


#output phase
print("The make and model of the entered Car is", make, model )
print("The msrp amount given is $",msrp)
print("The discount off the car displayed as a decimal value is", discpercent)
print("The amount off after the discount will be $", amtoff)
print("The discounted price of the car after deductions be $", discprice)