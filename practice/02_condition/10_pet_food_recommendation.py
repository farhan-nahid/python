def recommend_pet_food(species, age):
  species = species.lower().strip()
  
  if species == "dog":
    if age < 2:
      return "Puppy food"
    elif age >= 2 and age < 7:
      return "Adult dog food"
    else:
      return "Senior dog food"
  
  elif species == "cat":
    if age < 1:
      return "Kitten food"
    elif age >= 1 and age <= 5:
      return "Adult cat food"
    else:
      return "Senior cat food"
  
  else:
    return "Unknown species. Please specify Dog or Cat."