def fruit_ripeness_checker(fruit_dict):
  for key in fruit_dict:
    if fruit_dict[key] == "Green":
      print("Unripe")
    elif fruit_dict[key] == "Yellow":
      print("Ripe")
    elif fruit_dict[key] == "Brown":
      print("Overripe")
    else:
      print("Unknown")


fruit_ripeness_checker({'Banana': "Green"})