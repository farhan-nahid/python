# 9. Palindrome Number

## Problem Description

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A palindrome is a number that reads the same backward as forward.

## Examples

### Example 1:
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

### Example 2:
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

## Constraints

- `-2³¹ <= x <= 2³¹ - 1`

## Approach

1. **Handle negative numbers**: All negative numbers are not palindromes (due to the '-' sign)
2. **Reverse the number**: Extract digits from right to left and build the reversed number
3. **Compare**: Check if the reversed number equals the original number

### Key Insights:
- Negative numbers can never be palindromes
- We reverse the entire number without converting to string
- Use modulo (%) to extract the last digit
- Use integer division (//) to remove the last digit

## Complexity Analysis

- **Time Complexity**: O(log₁₀(x))
  - We divide the number by 10 in each iteration
  - Number of iterations is equal to the number of digits in x

- **Space Complexity**: O(1)
  - Only uses a constant amount of extra space for variables

## Follow-up

**Could you solve it without converting the integer to a string?**

Yes! The solution in `main.py` solves this problem without string conversion by mathematically reversing the number.

## Solution

See `main.py` for the implementation.