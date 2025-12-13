# Frequency Counting with Hashing

## Problem Description

Given two lists of integers:
- `n`: the list in which you want to count the frequency of each number
- `m`: the list of queries for which you want to print the frequency from `n`

For each number in `m`, print how many times it appears in `n`.

## Examples

### Example 1:
```
Input:
	n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
	m = [10, 111, 1, 9, 5, 67, 2]
Output:
	10: 1
	111: 0
	1: 1
	9: 0
	5: 4
	67: 0
	2: 2
```

## Constraints
- All elements in `n` are integers between 0 and 10 (inclusive) for the list-based approach
- Both `n` and `m` can have up to $10^8$ elements (dictionary approach is required for large/unbounded values)

## Approaches

### 1. Using a List (for small, bounded values)
	- Create a list of size 11 (for numbers 0 to 10)
	- Increment the count at the index corresponding to each number in `n`
	- For each query in `m`, print the count from the list (or 0 if out of bounds)

### 2. Using a Dictionary (for large or unbounded values)
	- Use a dictionary to store the frequency of each number in `n`
	- For each query in `m`, print the count from the dictionary (or 0 if not present)

## Complexity Analysis
- **Time Complexity**: $O(N + M)$
	- $N$ = length of `n`, $M$ = length of `m`
- **Space Complexity**: $O(K)$
	- $K$ = number of unique elements in `n` (list: $O(1)$ for small range, dict: $O(K)$ for large range)

## Solution
See `main.py` for both implementations: `count_frequency_with_list` and `count_frequency_with_dict`.
