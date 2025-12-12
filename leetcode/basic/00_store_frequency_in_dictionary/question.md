# Store Frequency in Dictionary

## Problem Description

Given a list of integers, count the frequency of each unique number and store the result in a dictionary (hash map).

## Examples

### Example 1:
```
Input: nums = [1, 2, 3, 4, 5, 1, 2]
Output: {1: 2, 2: 2, 3: 1, 4: 1, 5: 1}
Explanation: 1 and 2 appear twice, others appear once.
```

### Example 2:
```
Input: nums = [7, 7, 7]
Output: {7: 3}
Explanation: 7 appears three times.
```

### Example 3:
```
Input: nums = []
Output: {}
Explanation: Empty list returns an empty dictionary.
```

## Constraints

- $0 \leq$ length of nums $\leq 10^5$
- Each element in nums is an integer

## Approaches

### Approach 1: If-Else Check
1. Initialize an empty dictionary
2. For each number in the list:
	 - If the number is already a key, increment its value
	 - Otherwise, add it with value 1
3. Return the dictionary

### Approach 2: Using `dict.get()`
1. Initialize an empty dictionary
2. For each number in the list:
	 - Use `hash_map.get(num, 0) + 1` to increment or initialize
3. Return the dictionary

## Complexity Analysis

- **Time Complexity**: $O(n)$
	- One pass through the list
- **Space Complexity**: $O(k)$
	- $k$ is the number of unique elements

## Solution

See `main.py` for both implementations.
