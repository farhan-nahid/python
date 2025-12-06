def age_group_categorization(age):
  if age < 13:
    print('Child')
  elif age >= 13 and age <=19:
    print('Teenager')
  elif age >= 20 and age <=59:
    print('Adult')
  elif age >= 60:
    print('Senior')


age_group_categorization(25)