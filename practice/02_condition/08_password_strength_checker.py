def password_strength_checker(password):
  password_len = len(password)

  if password_len < 6:
    print("Weak")
  elif password_len <=10:
    print("Medium")
  else:
    print("Strong")