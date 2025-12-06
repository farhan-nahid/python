def grade_calculator(score):
  if score >= 101:
    print("Not a valid score")
  elif score <= 90:
    print("A")
  elif score <= 80:
    print("B")
  elif score <= 70:
    print("C")
  elif score <=60:
    print("D")
  else:
    print("F")


grade_calculator(100)