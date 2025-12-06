def transportation_mode_selection(distance):
  if distance < 3:
    print("Walk")
  elif distance <= 15:
    print("Bike")
  else:
    print("Car")