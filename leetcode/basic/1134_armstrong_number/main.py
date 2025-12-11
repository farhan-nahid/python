"""
        Check if x is an Armstrong number.
        Armstrong number:
            Sum of each digit raised to total number of digits = original number.

        Example:
            153 → 1³ + 5³ + 3³ = 153

        Time Complexity (TC): O(log₁₀(x))
            - One loop that extracts digits.

        Space Complexity (SC): O(1)
            - Only uses constant variables.
        """


class Solution:
    @staticmethod
    def count(n:int) -> int:
        num = n
        count = 0

        while num > 0:
            num = num // 10
            count += 1
        
        return count


    def is_armstrong_number(self, x:int) -> bool:
        length = self.count(x)
        num = x
        result = 0


        while num > 0:
            single = num % 10
            num = num // 10

            result += single ** length

        return result == x



prob1 = Solution()

print(prob1.is_armstrong_number(153))
print(prob1.is_armstrong_number(154))


