class Solution:
    def reverse(self, x: int) -> int:
        """
            Reverses digits of an integer while maintaining its sign.

            Time Complexity (TC): O(log₁₀(x))
                - Each step removes one digit (divide by 10).

            Space Complexity (SC): O(1)
                - Only simple variables used.

            Handles:
            - Negative numbers
            - Trailing zeros
        """

        num = abs(x)
        reversed_num = 0
        sign = -1 if x < 0 else 1

        while num != 0:
            last_num = num % 10
            num = num // 10
            reversed_num = (reversed_num * 10) + last_num

        if reversed_num > 2 ** 31 - 1 or reversed_num < -2 ** 31:
            return 0

        return reversed_num * sign
    

prob = Solution()

print(prob.reverse(123))
print(prob.reverse(-123))
print(prob.reverse(120))