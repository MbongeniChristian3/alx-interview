#!/usr/bin/python3
"""
Function to generate Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row

    for i in range(1, n):
        # Start the row with a 1
        row = [1]

        # Add the sum of the two elements above the current element
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        # End the row with a 1
        row.append(1)

        # Append the row to the triangle
        triangle.append(row)

    return triangle
