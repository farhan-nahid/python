# def movie_ticket_pricing(age, day):
#   if age >= 18 and day == 'Wednesday':
#     print('Ticket price is $10')
#   elif age >= 18:
#     print('Ticket price is $12')
#   elif day == 'Wednesday':
#     print('Ticket price is $6')
#   else:
#     print('Ticket price is $8')


def movie_ticket_pricing(age, day):
  price = 12 if age >= 18 else 8

  if(day == 'Wednesday'):
    price -= 2

  print(f'Ticket price is ${price}')


movie_ticket_pricing(25, 'Wednesday')