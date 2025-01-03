#### ground shipping

weight = int(input(" Enter the weight : "))

total_cost = 0

if weight <= 2:
    total_cost = (weight * 1.50) + 20
elif weight <= 6:
    total_cost = (weight * 3) + 20
elif weight <= 10:
    total_cost = (weight * 4) + 20
elif(weight > 10 ):
    total_cost = (weight * 4.75) + 20

print(total_cost)


#### Drone shipping
print("drone shiping")

weight1 = int(input("Enter the weight1 : "))
drone_ship_total = 0

if weight1 <= 2:
    drone_ship_total = weight1 * 4.50
elif weight1 <= 6:
    drone_ship_total = weight1 * 9
elif weight1 <= 10:
    drone_ship_total = weight1 * 12
elif(weight1 > 10):
    drone_ship_total = weight1 * 14.25

print(drone_ship_total)
