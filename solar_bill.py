#wap in python to calculate how much you earned from the generated unit.

cosumer_name = input("Enter the name of the consumer : ")
units = int(input("Enter the generated units : "))
bill = 0

#now we will use the if else statementes to stat the conditions.

if(units<100):  #if unit is <100 we have to pay 1.5rs for each one.
    bill = units*1.5
elif(units>100 and units<300):  #if unit is >100 and <300 we have to pay 2.5rs for each one.
    bill = units*2.5
elif(units>300 and units<500):  #if unit is >300 and <300 we have to pay 3.5rs for each one.
    bill = units*3.5
elif(units>500):    #if unit is >500 we have to pay 4rs for each one.
    bill = units*4
else:
    print("THE UNITS ARE NOT APPLACABLE...")

print("The name of the consumer : " , cosumer_name)
print("The generated units are : " , units)
print("So the total amount you generated from units are : " "₹" , bill)

    