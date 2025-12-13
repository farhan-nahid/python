# 1134. Armstrong Number

## Problem Description

Given an integer `n`, return `true` if and only if it is an **Armstrong number**.

An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

## Examples

### Example 1:
```
Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
```

### Example 2:
```
Input: n = 154
Output: false
Explanation: 154 is a 3-digit number, and 154 ≠ 1³ + 5³ + 4³ = 1 + 125 + 64 = 190
```

### Example 3:
```
Input: n = 9
Output: true
Explanation: 9 is a 1-digit number, and 9 = 9¹ = 9
```

## Constraints

- `1 <= n <= 10^8`

## Approach

1. **Count the digits**: First, determine how many digits are in the number
2. **Calculate the sum**: Extract each digit and raise it to the power of the total digit count
3. **Compare**: Check if the calculated sum equals the original number

## Complexity Analysis

- **Time Complexity**: O(log₁₀(n))
  - We iterate through each digit of the number once
  - The number of digits in n is log₁₀(n)

- **Space Complexity**: O(1)
  - Only uses constant extra space for variables

## Solution

See `main.py` for the implementation.
