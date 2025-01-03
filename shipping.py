
weight = int(input("Enter the weight of your package in pounds: "))

print("Ground Shipping:")
if weight <= 2:
    ground_shipping_cost = weight * 1.50 + 20.00
elif weight <= 6:
    ground_shipping_cost = weight * 3.00 + 20.00
elif weight <= 10:
    ground_shipping_cost = weight * 4.00 + 20.00
else:
    ground_shipping_cost = weight * 4.75 + 20.00
print(f"Cost: ${ground_shipping_cost:.2f}")


premium_ground_shipping_cost = 125.00
print(premium_ground_shipping_cost)


print("Drone Shipping:")
if weight <= 2:
    drone_shipping_cost = weight * 4.50
elif weight <= 6:
    drone_shipping_cost = weight * 9.00
elif weight <= 10:
    drone_shipping_cost = weight * 12.00
else:
    drone_shipping_cost = weight * 14.25
print(drone_shipping_cost)


cheapest_method = "Ground Shipping"
cheapest_cost = ground_shipping_cost

if drone_shipping_cost < cheapest_cost:
    cheapest_method = "Drone Shipping"
    cheapest_cost = drone_shipping_cost

if premium_ground_shipping_cost < cheapest_cost:
    cheapest_method = "Premium Ground Shipping"
    cheapest_cost = premium_ground_shipping_cost


print("This is the cheap method",cheapest_method)
