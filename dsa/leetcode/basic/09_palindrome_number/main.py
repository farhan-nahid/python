"""
        Checks whether an integer is a palindrome by reversing the number.

        Time Complexity (TC): O(log₁₀(x))
            - We divide the number by 10 in each iteration.
            - Number of iterations ≈ number of digits in x.

        Space Complexity (SC): O(1)
            - Only uses a few integer variables; no extra data structures.
        """


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes due to the '-' sign.
        if x < 0:
            return False

        num = x
        result = 0

        while num > 0:
            last_num = num % 10
            num = num // 10
            result = (result * 10) + last_num
        
        return result == x


prob1 = Solution()

print(prob1.isPalindrome(123))   # False
print(prob1.isPalindrome(121))   # True
print(prob1.isPalindrome(-121))  # False
