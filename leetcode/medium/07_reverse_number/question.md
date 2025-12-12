# 7. Reverse Integer

## Problem Description

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range [$-2^{31}$, $2^{31} - 1$], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Examples

### Example 1:
```
Input: x = 123
Output: 321
```

### Example 2:
```
Input: x = -123
Output: -321
```

### Example 3:
```
Input: x = 120
Output: 21
```

### Example 4:
```
Input: x = 0
Output: 0
```

## Constraints

- $-2^{31} \leq x \leq 2^{31} - 1$

## Approach

1. **Handle sign**: Store the sign and work with the absolute value.
2. **Reverse digits**: Extract digits one by one and build the reversed number.
3. **Check overflow**: If the reversed number is outside the 32-bit signed integer range, return 0.
4. **Return with sign**: Multiply the reversed number by the original sign.

**Key Insights:**
- Negative numbers are handled by storing the sign.
- Trailing zeros are automatically removed during reversal.
- No string conversion is used; all operations are mathematical.

## Complexity Analysis

- **Time Complexity**: $O(\log_{10}(x))$
    - Each iteration processes one digit.
- **Space Complexity**: $O(1)$
    - Only a constant number of variables are used.

## Solution

See `main.py` for the implementation.

