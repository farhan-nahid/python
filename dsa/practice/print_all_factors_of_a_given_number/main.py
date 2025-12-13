from math import sqrt


class Solution:
    def allFactors(self, x: int) -> list:
        """
        Brute Force Approach:
        Check all numbers from 1 to x.

        Time Complexity (TC): O(x)
            - Loop runs x times.

        Space Complexity (SC): O(k)
            - k = number of factors found.
        """
        result = []

        for i in range(1, x + 1):
            if x % i == 0:
                result.append(i)

        return result



    def allFactorsBetter(self, x: int) -> list:
        """
        Slightly Optimized Approach:
        We only check up to x/2 because no number > x/2 (except x itself)
        can divide x.

        Time Complexity (TC): O(x/2) → O(x)
            - Roughly half the operations of brute force.

        Space Complexity (SC): O(k)
        """
        result = []

        for i in range(1, int(x / 2) + 1):
            if x % i == 0:
                result.append(i)
        
        result.append(x)
        return result



    def allFactorsOptimal(self, x: int) -> list:
        """
        Optimal Approach using Square Root:
        Every factor <= sqrt(x) has a corresponding factor >= sqrt(x).

        Example: For x = 36:
            1 ↔ 36
            2 ↔ 18
            3 ↔ 12
            4 ↔ 9
            6 ↔ 6  (only once)

        Time Complexity (TC): O(sqrt(x))
            - Loop only runs up to sqrt(x).

        Space Complexity (SC): O(k)
            - Stores factors.

        Note: Factors are returned sorted.
        """
        result = []

        for i in range(1, int(sqrt(x)) + 1):
            if x % i == 0:
                result.append(i)

                division = x // i
                if division != i:  # avoid duplicates for perfect square
                    result.append(division)

        return sorted(result)



prob1 = Solution()

print(prob1.allFactors(36))
print(prob1.allFactorsBetter(36))
print(prob1.allFactorsOptimal(36))
