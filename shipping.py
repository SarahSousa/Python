weight = 41.5

#prices for ground shipping

flat_charge_ground = 20
cost_ground_under_2 = weight*1.50 + flat_charge_ground
cost_ground_under_6 = weight*3 + flat_charge_ground
cost_ground_under_10 = weight*4 + flat_charge_ground
cost_ground_over_10 = weight*4.75 + flat_charge_ground

#prices for ground shipping premium

cost_ground_premium = 125

#prices for drone shipping

cost_drone_under_2 = weight*4.50 
cost_drone_under_6 = weight*9
cost_drone_under_10 = weight*12
cost_drone_over_10 = weight*14.25 

#ground shipping

if weight <=2:
  print("Standard ground shipping: $" + str(cost_ground_under_2))
elif weight <= 6:
  print("Standard ground shipping: $" + str(cost_ground_under_6))
elif weight <= 10:
  print("Standard ground shipping: $" + str(cost_ground_under_10))
else:
  print("Standard ground shipping: $" + str(cost_ground_over_10))

#premium shipping
print("Premium ground shipping: $" + str(cost_ground_premium))

#premium shipping

if weight <=2:
  print("Drone shipping: $" + str(cost_drone_under_2))
elif weight <= 6:
  print("Drone shipping: $" + str(cost_drone_under_6))
elif weight <= 10:
  print("Drone shipping: $" + str(cost_drone_under_10))
else:
  print("Drone shipping: $" + str(cost_drone_over_10))

