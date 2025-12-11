from math import log10


"""
    Counts the number of digits in an integer using repeated division.

    Time Complexity (TC): O(log₁₀(n))
        - In each iteration, n is divided by 10.
        - Number of iterations ≈ number of digits = log₁₀(n).

    Space Complexity (SC): O(1)
        - Uses a constant amount of extra space.
    """


def count(n):
    num = n
    count = 0

    while num > 0:
        num = num // 10
        count += 1

    return count

print(count(54381233))




def count_with_log(n):
    return int(log10(n) + 1)


print(count_with_log(1234))