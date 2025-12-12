class Solution:
    def method1(self, nums: list[int]) -> dict:
        """
        Count frequency of each number using an if-else check.

        Time Complexity (TC): O(n)
            - Loop runs once for each element.

        Space Complexity (SC): O(k)
            - k = number of unique elements in nums.
            - Uses a dictionary to store counts.
        """

        hash_map = {}

        for i in range(len(nums)):
            # If number already exists, increment its count
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                # Otherwise initialize count to 1
                hash_map[nums[i]] = 1
        
        return hash_map



    def method2(self, nums: list[int]) -> dict:
        """
        Count frequency using hash_map.get() for cleaner code.

        Time Complexity (TC): O(n)
            - Still one pass through the list.

        Space Complexity (SC): O(k)
            - Same as method1.
        """

        hash_map = {}

        for i in range(len(nums)):
            # get(key, default_value) returns value if exists,
            # otherwise returns default_value (0 here)
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1

        return hash_map




prob = Solution()
print(prob.method1([1, 2, 3, 4, 5, 1, 2]))
print(prob.method2([1, 2, 3, 4, 5, 1, 2]))
