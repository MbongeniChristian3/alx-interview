#!/usr/bin/env python3


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current = n

    # Loop to find the factors of n
    for i in range(2, n + 1):
        while current % i == 0:
            operations += i  # Copy All + (i - 1) Pasts
            current //= i  # Reduce the number of Hs to be formed

    return operations

# Test the function
if __name__ == "__main__":
    print("Min number of operations to reach 4 characters:", minOperations(4))  # Output: 4
    print("Min number of operations to reach 12 characters:", minOperations(12))  # Output: 7
