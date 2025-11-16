import sys

def calculate_sum_and_average(scores=[10, 20, 30]):
    """Calculate sum and average of the score list."""
    total = sum(scores)
    avg = total / len(scores)
    return total, avg


def calculate_max_and_min(scores=[10, 20, 30]):
    """Calculate maximum and minimum score."""
    maximum = max(scores)
    minimum = min(scores)
    return maximum, minimum


