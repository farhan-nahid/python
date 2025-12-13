# Print All Factors of a Given Number

## Problem Description

Given a positive integer `x`, find and return all factors (divisors) of `x`.

A factor of a number is an integer that divides the number evenly (with no remainder).

## Examples

### Example 1:
```
Input: x = 36
Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]
Explanation: All these numbers divide 36 evenly.
```

### Example 2:
```
Input: x = 12
Output: [1, 2, 3, 4, 6, 12]
Explanation: 1×12, 2×6, 3×4 all equal 12.
```

### Example 3:
```
Input: x = 1
Output: [1]
Explanation: 1 is the only factor of 1.
```

## Constraints

- `1 <= x <= 10^9`

## Approaches

### Approach 1: Brute Force
Check every number from 1 to n to see if it divides n evenly.

**Algorithm**:
1. Iterate from 1 to n (inclusive)
2. If `x % i == 0`, add i to the result
3. Return the result list

**Complexity**:
- **Time Complexity**: O(n)
- **Space Complexity**: O(k) where k is the number of factors

### Approach 2: Optimized (Half Range)
Since factors come in pairs, we only need to check up to n/2.

**Algorithm**:
1. Iterate from 1 to n/2 (inclusive)
2. If `x % i == 0`, add i to the result
3. Add n itself at the end
4. Return the result list

**Key Insight**: If `i` is a factor where `i < n`, then `n/i > 1`. The largest factor less than n itself is n/2.

**Complexity**:
- **Time Complexity**: O(n/2) = O(n)
- **Space Complexity**: O(k) where k is the number of factors

### Approach 3: Optimal (Square Root)
Factors come in pairs, and we only need to check up to √n.

**Algorithm**:
1. Iterate from 1 to √n (inclusive)
2. If `x % i == 0`:
   - Add i to the result
   - Calculate the pair factor: `division = x // i`
   - If `division != i`, add division to the result (avoid duplicates for perfect squares)
3. Return the result list

**Key Insight**: For any factor `i` where `i ≤ √n`, there exists a corresponding factor `n/i` where `n/i ≥ √n`. For perfect squares, when `i = √n`, both factors are the same.

**Example with 36**:
- i = 1: factors are 1 and 36
- i = 2: factors are 2 and 18
- i = 3: factors are 3 and 12
- i = 4: factors are 4 and 9
- i = 6: factors are 6 and 6 (only add once)

**Complexity**:
- **Time Complexity**: O(√n)
- **Space Complexity**: O(k) where k is the number of factors

## Complexity Comparison

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n) | O(k) |
| Half Range | O(n/2) | O(k) |
| Optimal | O(√n) | O(k) |

Note: The optimal approach is significantly faster for large numbers. For example, if n = 1,000,000:
- Brute Force: 1,000,000 iterations
- Half Range: 500,000 iterations
- Optimal: ~1,000 iterations

## Solution

See `main.py` for all three implementations.