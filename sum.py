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
def main(scores=None):
    # If scores are provided from command line → use them
    if len(sys.argv) > 1:
        try:
            # Read scores from command line arguments
            scores = list(map(float, sys.argv[1:]))
        except ValueError:
            print("Error: Command line scores must be numbers.")
            sys.exit(1)

    # If no CLI arguments and no function parameter → use default values
    if scores is None:
        scores = [10, 20, 30]        # Default scores

    total, avg = calculate_sum_and_average(scores)
    maximum, minimum = calculate_max_and_min(scores)

    print("\n--- Program Output ---")
    print(f"Scores used: {scores}")
    print(f"Sum of scores: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Maximum score: {maximum}")
    print(f"Minimum score: {minimum}")


if __name__ == "__main__":
    main()
