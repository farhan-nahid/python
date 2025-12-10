def check_palindrome(n):
  num = n
  result =0

  while num > 0:
    last = num % 10
    num = num // 10
    result = (result * 10) + last

  return result == n


print(check_palindrome(1221))
print(check_palindrome(1222))