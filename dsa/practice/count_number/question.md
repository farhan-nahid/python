# Count Number of Digits

## Problem Description

Given a positive integer `n`, count and return the number of digits in `n`.

## Examples

### Example 1:
```
Input: n = 54381233
Output: 8
Explanation: The number 54381233 has 8 digits.
```

### Example 2:
```
Input: n = 1234
Output: 4
Explanation: The number 1234 has 4 digits.
```

### Example 3:
```
Input: n = 5
Output: 1
Explanation: The number 5 has 1 digit.
```

## Constraints

- `1 <= n <= 10^9`

## Approaches

### Approach 1: Iterative Division
1. Initialize a counter to 0
2. Repeatedly divide the number by 10
3. Increment the counter for each division
4. Continue until the number becomes 0
5. Return the counter

**Key Insight**: Each division by 10 removes one digit from the number.

### Approach 2: Logarithmic Formula
Use the mathematical formula: `floor(log₁₀(n)) + 1`

**Key Insight**: The number of digits in `n` is equal to `⌊log₁₀(n)⌋ + 1`.

## Complexity Analysis

### Approach 1 (Iterative):
- **Time Complexity**: O(log₁₀(n))
  - In each iteration, we divide n by 10
  - Number of iterations equals the number of digits = log₁₀(n)

- **Space Complexity**: O(1)
  - Uses constant extra space for variables

### Approach 2 (Logarithmic):
- **Time Complexity**: O(1)
  - Direct mathematical computation

- **Space Complexity**: O(1)
  - Uses constant extra space

## Solution

See `main.py` for both implementations.