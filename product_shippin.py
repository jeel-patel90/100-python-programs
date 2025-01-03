
weight = int(input("Enter the weight of the package : "))


print("Ground Shipping")


if weight <= 2:
    ground_cost = 20 + (1.50 * weight)
elif weight <= 6:
    ground_cost = 20 + (3.00 * weight)
elif weight <= 10:
    ground_cost = 20 + (4.00 * weight)
else:
    ground_cost = 20 + (4.75 * weight)

print(ground_cost)

ground_premium_cost = 125.00
print(ground_premium_cost)


print("Drone Shipping")


if weight <= 2:
    drone_cost = 4.50 * weight
elif weight <= 6:
    drone_cost = 9.00 * weight
elif weight <= 10:
    drone_cost = 12.00 * weight
else:
    drone_cost = 14.25 * weight

print(drone_cost)



